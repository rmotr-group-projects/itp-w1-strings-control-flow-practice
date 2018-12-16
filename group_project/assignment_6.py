# Example. Use it as a base to build your own template.
BOARD_TEMPLATE = """
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
"""


def format_tic_tac_toe_board(first_row, second_row, third_row):
    row_1_1 = first_row[0:1]
    row_1_2 = first_row[1:2]
    row_1_3 = first_row[2:3]
    row_2_1 = second_row[0:1]
    row_2_2 = second_row[1:2]
    row_2_3 = second_row[2:3]
    row_3_1 = third_row[0:1]
    row_3_2 = third_row[1:2]
    row_3_3 = third_row[2:3]
    board = BOARD_TEMPLATE.format(row_1_1,row_1_2,row_1_3,row_2_1,row_2_2,row_2_3,row_3_1,row_3_2,row_3_3)
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
