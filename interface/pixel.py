from abc import ABC, abstractmethod


class Pixel(ABC):
    @abstractmethod
    def get_color_depth(self) -> int:
        ...
    @abstractmethod
    def to_bytes(self) -> list[int]:
        ...
    @abstractmethod
    def get_padding(self) -> int:
        ...