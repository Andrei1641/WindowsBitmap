from pixel import Pixel
from tools import CreationProver, Translator


class WinHeader:
    def __init__(self, bfSize: int, bfReserved: int, bfOffbits: int, biSize: int, biWith: int, biHight: int,
                 biPlanes: int, biBitCount: int, biCompression: int, biSizeImage: int, biXPelsPerMeter: int,
                 biYPelsPerMeter: int, biClrUsed: int, biClrImportant: int):
        self.__bfType: int = 19778
        self.set_bfSize(bfSize)
        self.set_bfReserved(bfReserved)
        self.set_bfOffBits(bfOffbits)

        self.set_biSize(biSize)
        self.set_biWidth(biWith)
        self.set_biHeight(biHight)
        self.set_biPlanes(biPlanes)
        self.set_biBitCount(biBitCount)
        self.set_biCompression(biCompression)
        self.set_biSizeImage(biSizeImage)
        self.set_biXPelsPerMeter(biXPelsPerMeter)
        self.set_biYPelsPerMeter(biYPelsPerMeter)
        self.set_biClrUsed(biClrUsed)
        self.set_biClrImportant(biClrImportant)

    @staticmethod
    def translate_attr_in_byte_getter(attr: int, bytes_border: int) -> list[int]:
        attr_bytes: list[int] = Translator.from_int_to_bytes(attr)
        attr_bytes_filled: list[int] = Translator.fill_bytes_border(attr_bytes, bytes_border)
        return Translator.translate_endian(attr_bytes_filled)

    def get_bfType(self) -> list[int]:
        return WinHeader.translate_attr_in_byte_getter(self.__bfType, 2)

    def get_bfSize(self) -> list[int]:
        return WinHeader.translate_attr_in_byte_getter(self.__bfSize, 4)


    def set_bfSize(self, bfSize: int):
        if CreationProver.is_out_of_border(4, bfSize):
            self.__bfSize = bfSize
        else:
            raise ValueError('too much bytes are used')


    def get_bfReserved(self) -> list[int]:
        return WinHeader.translate_attr_in_byte_getter(self.__bfReserved, 4)

    def set_bfReserved(self, bfReserved: int):
        if CreationProver.is_out_of_border(4, bfReserved):
            self.__bfReserved = bfReserved
        else:
            raise ValueError('too much bytes are used')


    def get_bfOffBits(self) -> list[int]:
        return WinHeader.translate_attr_in_byte_getter(self.__bfOffBits, 4)

    def set_bfOffBits(self, bfOffBits: int):
        if CreationProver.is_out_of_border(4, bfOffBits):
            self.__bfOffBits = bfOffBits
        else:
            raise ValueError('too much bytes are used')


    def get_biSize(self) -> list[int]:
        return WinHeader.translate_attr_in_byte_getter(self.__biSize, 4)

    def set_biSize(self, biSize: int):
        if CreationProver.is_out_of_border(4, biSize):
            self.__biSize = biSize
        else:
            raise ValueError('too much bytes are used')


    def get_biWidth(self) -> list[int]:
        return WinHeader.translate_attr_in_byte_getter(self.__biWidth, 4)

    def set_biWidth(self, biWidth: int):
        if CreationProver.is_out_of_border(4, biWidth):
            self.__biWidth = biWidth
        else:
            raise ValueError('too much bytes are used')


    def get_biHeight(self) -> list[int]:
        return WinHeader.translate_attr_in_byte_getter(self.__biHeight, 4)

    def set_biHeight(self, biHeight: int):
        if CreationProver.is_out_of_border(4, biHeight):
            self.__biHeight = biHeight
        else:
            raise ValueError('too much bytes are used')


    def get_biPlanes(self) -> list[int]:
        return WinHeader.translate_attr_in_byte_getter(self.__biPlanes, 2)

    def set_biPlanes(self, biPlanes: int):
        if CreationProver.is_out_of_border(2, biPlanes):
            self.__biPlanes = biPlanes
        else:
            raise ValueError('too much bytes are used')


    def get_biBitCount(self) -> list[int]:
        return WinHeader.translate_attr_in_byte_getter(self.__biBitCount, 2)

    def set_biBitCount(self, biBitCoutn: int):
        if CreationProver.is_out_of_border(2, biBitCoutn):
            self.__biBitCount = biBitCoutn
        else:
            raise ValueError('too much bytes are used')

    def get_biCompression(self) -> list[int]:
        return WinHeader.translate_attr_in_byte_getter(self.__biCompression, 4)

    def set_biCompression(self, biCompression: int):
        if CreationProver.is_out_of_border(4, biCompression):
            self.__biCompression = biCompression
        else:
            raise ValueError('too much bytes are used')

    def get_biSizeImage(self) -> list[int]:
        return WinHeader.translate_attr_in_byte_getter(self.__biSizeImage, 4)

    def set_biSizeImage(self, biSizeImage: int):
        if CreationProver.is_out_of_border(4, biSizeImage):
            self.__biSizeImage = biSizeImage
        else:
            raise ValueError('too much bytes are used')

    def get_biXPelsPerMeter(self) -> list[int]:
        return WinHeader.translate_attr_in_byte_getter(self.__biXPelsPerMeter, 4)

    def set_biXPelsPerMeter(self, biXPelsPerMeter: int):
        if CreationProver.is_out_of_border(4, biXPelsPerMeter):
            self.__biXPelsPerMeter = biXPelsPerMeter
        else:
            raise ValueError('too much bytes are used')

    def get_biYPelsPerMeter(self) -> list[int]:
        return WinHeader.translate_attr_in_byte_getter(self.__biYPelsPerMeter, 4)

    def set_biYPelsPerMeter(self, biYPelsPerMeter: int):
        if CreationProver.is_out_of_border(4, biYPelsPerMeter):
            self.__biYPelsPerMeter = biYPelsPerMeter
        else:
            raise ValueError('too much bytes are used')

    def get_biClrUsed(self) -> list[int]:
        return WinHeader.translate_attr_in_byte_getter(self.__biClrUsed, 4)

    def set_biClrUsed(self, biClrUsed: int):
        if CreationProver.is_out_of_border(4, biClrUsed):
            self.__biClrUsed = biClrUsed
        else:
            raise ValueError('too much bytes are used')

    def get_biClrImportant(self) -> list[int]:
        return WinHeader.translate_attr_in_byte_getter(self.__biClrImportant, 4)

    def set_biClrImportant(self, biClrImportant: int):
        if CreationProver.is_out_of_border(4, biClrImportant):
            self.__biClrImportant = biClrImportant
        else:
            raise ValueError('too much bytes are used')


class WinBody:
    def __init__(self, pixels: list[Pixel]):
        self.__pixels = pixels

    @property
    def pixels(self) -> list[Pixel]:
        return self.__pixels

    def get_color_deph(self) -> int:
        return self.__pixels[0].get_color_depth()

    def get_size_in_bits(self) -> int:
        return self.__pixels[0].get_color_depth() * len(self.__pixels)
