import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC

from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.display import Display, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
keyboard.modules = [encoder_handler]
keyboard.extensions.append(MediaKeys())

keyboard.col_pins = (board.D0, board.D1, board.D2)
keyboard.row_pins = (board.D10, board.D9, board.D8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler.pins = [(board.D6, board.D7, None)]
encoder_handler.map = [((KC.VOLU, KC.VOLD),)]
# OLED, add stuff later

driver = SSD1306(
    i2c=busio.I2C(board.D5, board.D4)
)

display = Display(
    display=driver,
    width=128,
    height=32, 
    flip = True, 
    flip_left = False,
    flip_right = False, 
    brightness=1, 
    brightness_step=0.1, 
    dim_time=20, 
    dim_target=0.1, 
    off_time=60, 
    powersave_dim_time=10, 
    powersave_dim_target=0.1, 
    powersave_off_time=30,
)

display.entries = [
    ImageEntry(image="mangopad.bmp",x=0,y=0)
]

keyboard.extensions.append(display)

keyboard.keymap = [
    [KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9]
    
]

if __name__ == '__main__':
    keyboard.go()