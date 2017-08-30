# Example. Use it as a base to build your own template.
BOARD_TEMPLATE = """
O  |  O  |  X
--------------
X  |  X  |  O
--------------
O  |  X  |  O
"""


def format_tic_tac_toe_board(first_row, second_row, third_row):
    row = "--------------"
    new_first_row = '\n' + first_row[0] + "  |  " + first_row[1] + "  |  " + first_row[2] + "\n"
    
    new_second_row = '\n' + second_row[0] + "  |  " + second_row[1] + "  |  " + second_row[2] + "\n"
    
    new_third_row = '\n' + third_row[0] + "  |  " + third_row[1] + "  |  " + third_row[2] + "\n"
    board = new_first_row + row + new_second_row + row + new_third_row
    return board


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
