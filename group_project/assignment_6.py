# Example. Use it as a base to build your own template.
BOARD_TEMPLATE = """
O  |  O  |  X
--------------
X  |  X  |  O
--------------
O  |  X  |  O
"""


def format_tic_tac_toe_board(first_row, second_row, third_row):
    the_vertical_split = '  |  '
    the_horizontal_split = '-'* 14 +'\n'
    board = '\n'
    all_rows = (first_row, second_row, third_row)
    board += the_horizontal_split.join([the_vertical_split.join(rows)+ '\n' for rows in all_rows])
  
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
