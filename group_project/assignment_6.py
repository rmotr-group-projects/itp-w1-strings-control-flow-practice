# Example. Use it as a base to build your own template.
BOARD_TEMPLATE = """
O  |  O  |  X
--------------
X  |  X  |  O
--------------
O  |  X  |  O
"""


def format_tic_tac_toe_board(first_row, second_row, third_row):
# declare variables for each square in tic tac toe board
    r1c1 = first_row[0] 
    r1c2 = first_row[1]
    r1c3 = first_row[2] 
    
    r2c1 = second_row[0] 
    r2c2 = second_row[1] 
    r2c3 = second_row[2] 
    
    r3c1 = third_row[0]
    r3c2 = third_row[1]
    r3c3 = third_row[2]
    
    BOARD_TEMPLATE = """
    {}  |  {}  |  {}
    --------------
    {}  |  {}  |  {}
    --------------
    {}  |  {}  |  {}
    """
    
    return(BOARD_TEMPLATE.format(r1c1, r1c2, r1c3, r2c1, r2c2, r2c3, r3c1, r3c2, r3c3))


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


first_row = 'XOX'
second_row = 'OXO'
third_row = 'OOX'

print(format_tic_tac_toe_board(first_row, second_row, third_row))