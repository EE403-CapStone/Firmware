# Firmware
Peripherals configured in CircuitPython, utilizing KMK firmware.[^1]

Table of contents
=================

<!--ts-->
   * [Keyboard Module](#Keyboard-Module)
      * [Keyboard Firmware](#Keyboard-Firmware)
   * [NumPad Module](#NumPad-Module)
      * [NumPad Firmware](#NumPad-Firmware)
   * [Joystick Module](#Joystick-Module)
      * [Joystick Firmware](#Joystick-Firmware)
<!--te-->


Keyboard Module
===============

```
R0 | SW3     SW7     SW11    SW15    SW19    SW23    SW27    SW31    SW35    SW39
R1 | SW2     SW6     SW10    SW14    SW18    SW22    SW26    SW30    SW33    SW38
R2 | SW1     SW5     SW9     SW13    SW17    SW21    SW25    SW29    SW33    SW37
R3 | SW0     SW4     SW8     SW12    SW16    SW20    SW24    SW28    SW32    SW36
    -----------------------------------------------------------------------------
     C0      C1      C2      C3      C4      C5      C6      C7      C8      C9
```
Keyboard Firmware
-----------------

```
keyboard.keymap = [
    [
        KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,     KC.F10,
        KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,      KC.P,
        KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,      KC.BSPACE,
        KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.NO,   KC.RSHIFT, KC.RCTRL,
    ]
]
```

NumPad Module
=============

```
R0 | SW6     SW13    SW20 
R1 | SW5     SW12    SW19
R2 | SW4     SW11    SW18
R3 | SW3     SW10    SW17
R4 | SW2     SW9     SW16
R5 | SW1     SW8     SW15
R6 | SW0     SW7     SW14
    ---------------------
     C0      C1      C2
```

NumPad Firmware
---------------

```
keyboard.keymap = [
    [
        KC.F11,          KC.F12,       KC.F13,   
        KC.KP_ASTERICK,  KC.KP_SLASH,  KC.CIRCUMFLEX,    
        KC.KP_PLUS,      KC.KP_MINUS,  KC.KP_EQUAL,    
        KC.KP_7,         KC.KP_8,      KC.KP_9, 
        KC.KP_4,         KC.KP_5,      KC.KP_6, 
        KC.KP_1,         KC.KP_2,      KC.KP_3, 
        KC.KP_0,         KC.X,         KC.C, 
    ]
]
```

Joystick Module
===============

```
R0 |         SW3   
R1 | SW1             SW19
R2 |         SW2    

    ---------------------
     C0      C1      C2
```

Joystick Firmware
-----------------

[^1]: http://kmkfw.io
