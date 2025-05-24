from abc import ABC
from typing import Iterator

from unleash_the_geek_2024.template import StringifyInterface, MutableCollection


class BaseAction(StringifyInterface, ABC):
    ...


class ActionCollection(MutableCollection):
    def __iter__(self) -> Iterator[BaseAction]:
        return super().__iter__()

    def __str__(self):
        return ', '.join([str(action) for action in self])
