from abc import ABC
from typing import Iterator

from common.collection import MutableCollection
from common.stringify_interface import StringifyInterface


class BaseAction(StringifyInterface, ABC):
    ...


class ActionCollection(MutableCollection):
    def __iter__(self) -> Iterator[BaseAction]:
        return super().__iter__()
