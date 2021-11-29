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

    files_tree = ready_directory_and_build_info_tree(files_root_folder_path)
    for key, file_info in files_tree.items():
        if included_content != '':
            included_content += "\r\n"

        included_content += file_info['class_content']

    return included_content


def ready_directory_and_build_info_tree(base_path: str):
    info_tree = {}
    for file_path in glob.iglob(base_path + '**/**', recursive=True):
        if file_path.find('.py') == -1:
            continue

        if file_path.find('__init__.py') > -1:
            continue

        file_infos = get_file_infos(file_path)
        for key, value in file_infos.items():
            info_tree[key] = value

    return info_tree


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
            'dependencies': get_class_dependencies(class_name, file_content)
        }

    return file_infos


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


def get_class_dependencies(class_name, file_content):
    dependencies = []



if __name__ == '__main__':
    template_file_resource = open('./main.template.py', 'r')
    template_file_content = template_file_resource.read()
    template_file_resource.close()

    result_file_resource = open('./main.py', 'w')

    build(template_file_content, '{placeholder}', result_file_resource)
    result_file_resource.close()
