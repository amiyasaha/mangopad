import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation
from kmk.extensions.RGB import RGB
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP26, board.GP27, board.GP28)
keyboard.row_pins = (board.GP3, board.GP4, board.GP2)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

rgb = RGB(pixel_pin=board.GP29, num_pixels=9)

# OLED, add stuff later

driver = SSD1306(
    i2c= busio.I2C(board.GP7, board.GP6)
)

keyboard.extensions.append(rgb)

keyboard.keymap = [
    [KC.N1, KC.N2, KC.N3], 
    [KC.N4, KC.N5, KC.N6],
    [KC.N7, KC.N8, KC.N9]
    
]

if __name__ = '__main__':
    keyboard.go()