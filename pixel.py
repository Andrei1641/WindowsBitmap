from abc import ABC, abstractmethod


class Pixel(ABC):
    @abstractmethod
    def get_color_depth(self) -> int:
        ...

class Pixel24Bit(Pixel):
    def __init__(self):
        ...
    
    def get_color_depth(self) -> int:
        ...