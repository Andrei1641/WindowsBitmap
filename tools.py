import math

class Translator:
    @staticmethod
    def from_int_to_bytes(number: int) -> list[int]:
        number_of_bits: int = Translator.__get_number_of_bits_in_int(number)
        number_of_bytes: int = math.ceil(number_of_bits / 8)
        return list(number.to_bytes(number_of_bytes))

    @staticmethod
    def __get_number_of_bits_in_int(number: int) -> int:
        return math.ceil(math.log(number, 2))

    @staticmethod
    def translate_endian(b: list[int]) -> list[int]:
        return b[::-1]

    @staticmethod
    def fill_bytes_border(attr_bytes: list[int], bytes_border: int):
        if len(attr_bytes) < bytes_border:
            attr_bytes = [0] * (4 - len(attr_bytes)) + attr_bytes
        return attr_bytes


class CreationProver:
    @staticmethod
    def is_out_of_border(byte_number_border: int, number: int) -> bool:
        if number < 2 ** (8 * byte_number_border):
            return True
        return False