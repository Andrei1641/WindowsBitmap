from file_object import WinHeader, WinBody


class WinCreator:
    @staticmethod
    def create_header(win_header: WinHeader) -> list[bytes]:
        ...

    @staticmethod
    def create_body(win_body: WinBody) -> list[bytes]:
        ...

    @staticmethod
    def write_file(header: list[bytes], body: list[bytes]):
        ...