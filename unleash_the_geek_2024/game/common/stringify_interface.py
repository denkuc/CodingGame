from abc import ABC, abstractmethod


class StringifyInterface(ABC):
    @abstractmethod
    def to_string(self) -> str:
        ...
