# Example. Use it as a base to build your own template.
BOARD_TEMPLATE = """
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
"""


def format_tic_tac_toe_board(first_row, second_row, third_row):
    r1_c1=first_row[0]
    r1_c2=first_row[1]
    r1_c3=first_row[2]
    r2_c1=second_row[0]
    r2_c2=second_row[1]
    r2_c3=second_row[2]
    r3_c1=third_row[0]
    r3_c2=third_row[1]
    r3_c3=third_row[2]
    
    board=BOARD_TEMPLATE.format(r1_c1,r1_c2,r1_c3,r2_c1,r2_c2,r2_c3,r3_c1,r3_c2,r3_c3)
    
    return board
    
first_row='XOX'
second_row = 'OXO'
third_row = 'OOX'
    
board= format_tic_tac_toe_board(first_row,second_row,third_row)
print(board)


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