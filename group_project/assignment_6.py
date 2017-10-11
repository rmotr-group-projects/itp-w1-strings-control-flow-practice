# Example. Use it as a base to build your own template.
BOARD_TEMPLATE = """
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
"""


def format_tic_tac_toe_board(first_row, second_row, third_row):
    row_1 = first_row
    row_2 = second_row
    row_3 = third_row
    board = BOARD_TEMPLATE.format(
        row_1[0], row_1[1], row_1[2],
        row_2[0], row_2[1], row_2[2],
        row_3[0], row_3[1], row_3[2])
    return board

"""
def format_tic_tac_toe_board(first_row, second_row, third_row):
    row_1 = first_row
    row_2 = second_row
    row_3 = third_row
    result = ""
    result += row_1[0] + " | " + row_1[1] + " | " + row_1[2] + "\n"
    result += "---------" + "\n"
    result += row_2[0] + " | " + row_2[1] + " | " + row_2[2] + "\n"
    result += "---------" + "\n"
    result += row_3[0] + " | " + row_3[1] + " | " + row_3[2] + "\n"
    return result
"""

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