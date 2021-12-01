from entity.actions.base_action import BaseAction


class PassAction(BaseAction):
    def to_string(self) -> str:
        return 'PASS'
