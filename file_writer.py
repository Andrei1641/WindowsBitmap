from file_object import WinHeader, WinBody
from pixel import Pixel
from tools import Translator


class WinCreator:
    @staticmethod
    def create_header(win_header: WinHeader) -> list[int]:
        header_byte_list: list[int] = []
        header_byte_list += win_header.get_bfType()
        header_byte_list += win_header.get_bfSize()
        header_byte_list += win_header.get_bfReserved()
        header_byte_list += win_header.get_bfOffBits()
        header_byte_list += win_header.get_biSize()
        header_byte_list += win_header.get_biWidth()
        header_byte_list += win_header.get_biHeight()
        header_byte_list += win_header.get_biPlanes()
        header_byte_list += win_header.get_biBitCount()
        header_byte_list += win_header.get_biCompression()
        header_byte_list += win_header.get_biSizeImage()
        header_byte_list += win_header.get_biXPelsPerMeter()
        header_byte_list += win_header.get_biYPelsPerMeter()
        header_byte_list += win_header.get_biClrUsed()
        header_byte_list += win_header.get_biClrImportant()
        return header_byte_list

    @staticmethod
    def create_body(win_body: WinBody) -> list[int]:
        padding_per_row = win_body.get_padding() // win_body.height
        padding_per_row_in_byte = [0] * padding_per_row
        pixels: list[Pixel] = win_body.pixels
        pixels_in_bytes: list[int] = []
        row_pixel_counter = 0
        for pixel in pixels:
            pixels_in_bytes += pixel.to_bytes()
            row_pixel_counter += 1
            if row_pixel_counter == win_body.width:
                pixels_in_bytes += padding_per_row_in_byte
                row_pixel_counter = 0

        for pixel in pixels:
            pixels_in_bytes += pixel.to_bytes()
        return pixels_in_bytes


    @staticmethod
    def write_file(header: list[int], body: list[int]):
        with open('file.bmp', 'wb') as f:
            f.write(bytes(header))
            f.write(bytes(body))