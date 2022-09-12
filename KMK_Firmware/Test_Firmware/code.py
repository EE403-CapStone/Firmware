print("Starting")

import board

from analogio import AnalogIn
import usb_hid
from adafruit_hid.mouse import Mouse

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.handlers.sequences import send_string
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.combos import Combos, Chord, Sequence

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
keyboard.modules = [encoder_handler]

keyboard.col_pins = (board.GP1, board.GP2,)    # try D5 on Feather, keeboar
keyboard.row_pins = (board.GP0,)              # try D6 on Feather, keeboar
keyboard.diode_orientation = DiodeOrientation.COL2ROW



encoder_handler.pins = ((board.GP6, board.GP7, None, False),)

keyboard.tap_time = 250
keyboard.debug_enabled = False

sequence_1 = send_string("Rotary Encoder Is ")
sequence_2 = send_string("Working!")
secquence_3 = send_string("https://www.youtube.com/watch?v=b0FViwZmsGQ")

keyboard.modules.append(MouseKeys())

keyboard.keymap = [
    [secquence_3, KC.MB_LMB,]
]


encoder_handler.map = [
    ((sequence_1, sequence_2,),)
]



if __name__ == '__main__':
    keyboard.go()

