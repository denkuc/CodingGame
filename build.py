import glob
import re


def build(
        input_file_content: str,
        placeholder: str,
        output_file_resource
):
    new_added_content = get_included_content()
    output_file_resource.write(input_file_content.replace(placeholder, new_added_content))


def get_included_content():
    files_root_folder_path = './game'
    included_content = ''

    files_info_tree = read_directory_and_build_files_info_tree(files_root_folder_path)
    for file_info in files_info_tree:
        if included_content != '':
            included_content += "\r\n"

        included_content += file_info['class_content']

    return included_content


def read_directory_and_build_files_info_tree(base_path: str):
    files_info_tree = {}
    for file_path in glob.iglob(base_path + '**/**', recursive=True):
        if file_path.find('.py') == -1:
            continue

        if file_path.find('__init__.py') > -1:
            continue

        file_infos = get_file_infos(file_path)
        for key, value in file_infos.items():
            files_info_tree[key] = value

    for file_info in files_info_tree.values():
        setup_dependencies(file_info, files_info_tree.keys())

    files_info_tree = update_position(files_info_tree)

    sorted_files_info_tree = sorted(files_info_tree.values(), key=lambda d: d['position'])

    return sorted_files_info_tree


def get_file_infos(file_path):
    file_infos = {}
    file_resource = open(file_path, 'r')
    file_content = file_resource.read()
    file_resource.close()

    find_classes_result = re.findall(r'class ([a-zA-Z]+)', file_content, re.MULTILINE)
    for class_name in find_classes_result:
        file_infos[class_name] = {
            'path': file_path,
            'class_name': class_name,
            'class_content': get_class_content(class_name, file_content),
            'dependencies': [],
            'position': 0
        }

    return file_infos


def setup_dependencies(file_info, class_name_list):
    for class_name in class_name_list:
        if class_name == file_info['class_name']:
            continue

        if file_info['class_content'].find(class_name) == -1:
            continue

        file_info['dependencies'].append(class_name)
        
        
def update_position(files_info_tree: dict):
    is_position_updated = False
    for class_name, file_info in files_info_tree.items():
        if len(file_info['dependencies']) == 0:
            continue

        position = file_info['position']
        for dependency_name in file_info['dependencies']:
            dependency_position = files_info_tree[dependency_name]['position']
            if dependency_position >= position:
                position = dependency_position + 1

        if file_info['position'] != position:
            file_info['position'] = position
            is_position_updated = True

    if is_position_updated is True:
        return update_position(files_info_tree)

    return files_info_tree


def get_class_content(class_name, file_content):
    class_content_regex_with_multi_classes = r'class {}(.*?):(.*)(class)'.format(class_name)
    class_content_regex_with_one_class = r'class {}(.*?):(.*)'.format(class_name)

    class_content = ''
    find_class_content_result = re.search(class_content_regex_with_multi_classes, file_content, re.S)
    if not find_class_content_result:
        find_class_content_result = re.search(class_content_regex_with_one_class, file_content, re.S)
        if find_class_content_result:
            class_content = find_class_content_result.group(0)
    else:
        class_content = find_class_content_result.group(0)
        # need to remove last class text
        class_content = class_content[0:-5]

    return class_content


if __name__ == '__main__':
    template_file_resource = open('./main.template.py', 'r')
    template_file_content = template_file_resource.read()
    template_file_resource.close()

    result_file_resource = open('./main.py', 'w')

    build(template_file_content, '{placeholder}', result_file_resource)
    result_file_resource.close()
