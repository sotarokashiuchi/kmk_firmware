import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GPIO2, board.GPIO1, board.GPIO13, board.GPIO12, board.GPIO11, board.GPIO10, board.GPIO9,)
keyboard.row_pins = (board.GPIO38, board.GPIO39, board.GPIO40, board.GPIO41,)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

#					+-------------------+
#	+---+---+	3	|	4	|	5	|	6	|	7	|
#	|	1	|	2	+---+---+---+---+---+
#	+---+---+10	|11	|12	|13	|14	|
#	|	8	|	9	+---+---+---+---+---+	+---+
#	+---+---+17	|18	|19	|20	|21	|	|22	|
#	|15	|16	+---+---+---+---+---+-+-+-+
# +---+---+		|23	|24	|25	|26	|27	|
#							+---+---+---+---+---+

keyboard.keymap = [
    #	1,	2,	3,	4,	5,	6,	7,
    #	8,	9, 	10, 11, 12, 13, 14,
    #	15,	16,	17,	18,	19,	20,	21,
    # 27,	22,	-,	23,	24,	25,	26,
    [
        KC.A, KC.A, KC.Q, KC.W, KC.E, KC.R, KC.T,
        KC.A, KC.A, KC.A, KC.S, KC.D, KC.F, KC.G,
        KC.A, KC.A, KC.Z, KC.X, KC.C, KC.V, KC.B,
        KC.A, KC.A, KC.A, KC.A, KC.A, KC.A, KC.A,
    ]
]

if __name__ == '__main__':
    keyboard.go()
