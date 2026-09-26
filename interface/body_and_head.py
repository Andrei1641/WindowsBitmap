from abc import ABC, abstractmethod


class Body(ABC):
    @abstractmethod
    def get_body(self) -> list[int]:
        ...

    @abstractmethod
    def get_padding(self) -> int:
        ...

    @abstractmethod
    def get_color_deph(self) -> int:
        ...

class Header(ABC):
    @abstractmethod
    def get_header(self) -> list[int]:
        ...