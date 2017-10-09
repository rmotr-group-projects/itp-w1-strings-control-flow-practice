# Example. Use it as a base to build your own template.
BOARD_TEMPLATE = """
O  |  O  |  X
--------------
X  |  X  |  O
--------------
O  |  X  |  O
"""


def format_tic_tac_toe_board(first_row, second_row, third_row):
    row_1 = first_row
    row_2 = second_row
    row_3 = third_row
    print ("\n\t",row_1[0], "|", row_1[1], "|", row_1[2])
    print("\t", "---------")
    print("\t", row_2[0], "|", row_2[1], "|", row_2[2])
    print("\t", "---------")
    print("\t", row_3[0], "|", row_3[1], "|", row_3[2], "\n")


def test_format_board():
    """
    This is the board used in this test:
        X  |  O  |  X
        --------------
        O  |  X  |  O
        --------------
        O  |  O  |  X
    """
    first_row = 'XOX'
    second_row = 'OXO'
    third_row = 'OOX'
    expected_board = """
X  |  O  |  X
--------------
O  |  X  |  O
--------------
O  |  O  |  X
"""
    board = format_tic_tac_toe_board(first_row, second_row, third_row)

    assert board == expected_board