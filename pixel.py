from abc import ABC, abstractmethod

from tools import Translator


class Pixel(ABC):
    @abstractmethod
    def get_color_depth(self) -> int:
        ...
    @abstractmethod
    def to_bytes(self) -> list[int]:
        ...

class Pixel24Bit(Pixel):
    def __init__(self, red: int, green: int, blue: int):
        self.__red = red
        self.__green = green
        self.__blue = blue

    def get_color_depth(self) -> int:
        return 24

    def to_bytes(self) -> list[int]:
        pixel_in_bin: list[int] = []
        pixel_in_bin += Translator.from_int_to_bytes(self.__blue)
        pixel_in_bin += Translator.from_int_to_bytes(self.__green)
        pixel_in_bin += Translator.from_int_to_bytes(self.__red)
        return pixel_in_bin