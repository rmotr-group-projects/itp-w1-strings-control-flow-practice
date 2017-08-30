# Example. Use it as a base to build your own template.
BOARD_TEMPLATE = """
O  |  O  |  X
--------------
X  |  X  |  O
--------------
O  |  X  |  O
"""


def format_tic_tac_toe_board(first_row, second_row, third_row):
    
    start = '"""\n'
    end = '"""'
    
    row_one =   '0  |  1  |  2\n'
    row_two =   '3  |  4  |  5\n'
    row_three = '6  |  7  |  8\n'
    line_break = '--------------\n'
    
    row_one = row_one.replace('0', first_row[0])
    row_one = row_one.replace('1', first_row[1])
    row_one = row_one.replace('2', first_row[2])
    
    row_two = row_two.replace('3', second_row[0])
    row_two = row_two.replace('4', second_row[1])
    row_two = row_two.replace('5', second_row[2])
    
    row_three = row_three.replace('6', third_row[0])
    row_three = row_three.replace('7', third_row[1])
    row_three = row_three.replace('8', third_row[2])
    
    tictactoe = row_one + line_break + row_two + line_break +
                row_three
                
    return tictactoe


    return tictactoe
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
