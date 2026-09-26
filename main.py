from file_object import WinHeader, WinBody
from file_writer import WinCreator
from pixel import Pixel, Pixel24Bit

pixels: list[Pixel] = [Pixel24Bit(0, 0, 255), Pixel24Bit(0, 0, 255), Pixel24Bit(255, 0, 0), Pixel24Bit(255, 0, 0)]
win_body: WinBody = WinBody(pixels, 4, 1)

win_header: WinHeader = WinHeader(
    54 + (len(pixels) * 4), 0, 54, 40, win_body.width, win_body.height, 1, win_body.get_color_deph(), 0,
    (len(pixels) * 4), 0, 0, 0, 0
)



byte_header = WinCreator.create_header(win_header)
byte_body = WinCreator.create_body(win_body)

WinCreator.write_file(byte_header, byte_body)
