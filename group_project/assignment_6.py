# Example. Use it as a base to build your own template.
BOARD_TEMPLATE = """
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
"""

def format_tic_tac_toe_board(first_row, second_row, third_row):
    r1_1 = first_row[0]
    r1_2 = first_row[1]
    r1_3 = first_row[2]
    
    r2_1 = second_row[0]
    r2_2 = second_row[1]
    r2_3 = second_row[2]
    
    r3_1 = third_row[0]
    r3_2 = third_row[1]
    r3_3 = third_row[2]
    
    board = BOARD_TEMPLATE.format(
        r1_1, r1_2, r1_3,
        r2_1, r2_2, r2_3,
        r3_1, r3_2, r3_3,
    )
    
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
