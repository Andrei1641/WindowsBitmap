from interface.body_and_head import Body, Header
from objects.win_body_head import WinHeader, WinBody
from tools.file_writer import PictureCreator
from objects.pixel import Pixel, Pixel24Bit

pixels: list[Pixel] = [Pixel24Bit(0, 0, 255), Pixel24Bit(255, 255, 255), Pixel24Bit(255, 0, 0), Pixel24Bit(255, 0, 0)]
win_body: Body = WinBody(pixels, 4, 1)

win_header: Header = WinHeader(
    54 + (len(pixels) * 4), 0, 54, 40, win_body.get_width(), win_body.get_height(), 1, win_body.get_color_deph(), 0,
    (len(pixels) * 4), 0, 0, 0, 0
)



PictureCreator.write_file(win_header, win_body)
