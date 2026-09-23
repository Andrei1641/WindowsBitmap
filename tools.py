class Translator:
    @staticmethod
    def from_int_to_byte(integer: int) -> list[bytes]:
        ...
    @staticmethod
    def translate_endian(b: list[bytes]) -> list[bytes]:
        ...


class CreationProver:
    @staticmethod
    def is_out_of_border(byte_number_border: int, number: int) -> bool:
        ...