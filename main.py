from file_object import WinHeader, WinBody
from file_writer import WinCreator
from pixel import Pixel, Pixel24Bit

win_header: WinHeader = WinHeader(
    58, 0, 54, 40, 1, 1, 1, 24, 0,
    4, 0, 0, 0, 0
)

pixels: list[Pixel] = [Pixel24Bit(0, 255, 0)]
win_body: WinBody = WinBody(pixels)

byte_header = WinCreator.create_header(win_header)
byte_body = WinCreator.create_body(win_body)

WinCreator.write_file(byte_header, byte_body)
