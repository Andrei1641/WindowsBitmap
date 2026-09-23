from tools import CreationProver

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


    def get_bfType(self) -> int:
        return self.__bfType

    def get_bfSize(self) -> int:
        return self.__bfSize

    def set_bfSize(self, bfSize: int):
        if CreationProver.is_out_of_border(4, bfSize):
            self.__bfSize = bfSize
        else:
            raise ValueError('too much bytes are used')


    def get_bfReserved(self) -> int:
        return self.__bfReserved

    def set_bfReserved(self, bfReserved: int):
        if CreationProver.is_out_of_border(4, bfReserved):
            self.__bfReserved = bfReserved
        else:
            raise ValueError('too much bytes are used')


    def get_bfOffBits(self) -> int:
        return self.__bfOffBits

    def set_bfOffBits(self, bfOffBits: int):
        if CreationProver.is_out_of_border(4, bfOffBits):
            self.__bfOffBits = bfOffBits
        else:
            raise ValueError('too much bytes are used')


    def get_biSize(self) -> int:
        return self.__biSize

    def set_biSize(self, biSize: int):
        if CreationProver.is_out_of_border(4, biSize):
            self.__biSize = biSize
        else:
            raise ValueError('too much bytes are used')


    def get_biWidth(self) -> int:
        return self.__biWidth

    def set_biWidth(self, biWidth: int):
        if CreationProver.is_out_of_border(4, biWidth):
            self.__biWidth = biWidth
        else:
            raise ValueError('too much bytes are used')


    def get_biHeight(self) -> int:
        return self.__biHeight

    def set_biHeight(self, biHeight: int):
        if CreationProver.is_out_of_border(4, biHeight):
            self.__biHeight = biHeight
        else:
            raise ValueError('too much bytes are used')


    def get_biPlanes(self) -> int:
        return self.__biPlanes

    def set_biPlanes(self, biPlanes: int):
        if CreationProver.is_out_of_border(2, biPlanes):
            self.__biPlanes = biPlanes
        else:
            raise ValueError('too much bytes are used')


    def get_biBitCount(self) -> int:
        return self.__biBitCount

    def set_biBitCount(self, biBitCoutn: int):
        if CreationProver.is_out_of_border(2, biBitCoutn):
            self.__biBitCount = biBitCoutn
        else:
            raise ValueError('too much bytes are used')

    def get_biCompression(self) -> int:
        return self.__biCompression

    def set_biCompression(self, biCompression: int):
        if CreationProver.is_out_of_border(4, biCompression):
            self.__biCompression = biCompression
        else:
            raise ValueError('too much bytes are used')

    def get_biSizeImage(self) -> int:
        return self.__biSizeImage

    def set_biSizeImage(self, biSizeImage: int):
        if CreationProver.is_out_of_border(4, biSizeImage):
            self.__biSizeImage = biSizeImage
        else:
            raise ValueError('too much bytes are used')

    def get_biXPelsPerMeter(self) -> int:
        return self.__biXPelsPerMeter

    def set_biXPelsPerMeter(self, biXPelsPerMeter: int):
        if CreationProver.is_out_of_border(4, biXPelsPerMeter):
            self.__biXPelsPerMeter = biXPelsPerMeter
        else:
            raise ValueError('too much bytes are used')

    def get_biYPelsPerMeter(self) -> int:
        return self.__biYPelsPerMeter

    def set_biYPelsPerMeter(self, biYPelsPerMeter: int):
        if CreationProver.is_out_of_border(4, biYPelsPerMeter):
            self.__biYPelsPerMeter = biYPelsPerMeter
        else:
            raise ValueError('too much bytes are used')

    def get_biClrUsed(self) -> int:
        return self.__biClrUsed

    def set_biClrUsed(self, biClrUsed: int):
        if CreationProver.is_out_of_border(4, biClrUsed):
            self.__biClrUsed = biClrUsed
        else:
            raise ValueError('too much bytes are used')

    def get_biClrImportant(self) -> int:
        return self.__biClrImportant

    def set_biClrImportant(self, biClrImportant: int):
        if CreationProver.is_out_of_border(4, biClrImportant):
            self.__biClrImportant = biClrImportant
        else:
            raise ValueError('too much bytes are used')


class WinBody:
    def __init__(self):
        ...

    def get_color_deph(self) -> int:
        ...

    def get_size(self) -> int:
        ...
