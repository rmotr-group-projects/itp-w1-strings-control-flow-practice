# Example. Use it as a base to build your own template.
BOARD_TEMPLATE = """
O  |  O  |  X
--------------
X  |  X  |  O
--------------
O  |  X  |  O
"""

def format_tic_tac_toe_board(first_row, second_row, third_row):
    char = "  |  "
    lines_row = "--------------"
    new_first_row = char.join(first_row[i:i+1] for i in range(0, len(first_row)))
    new_second_row = char.join(second_row[i:i+1] for i in range(0, len(second_row)))
    new_third_row = char.join(third_row[i:i+1] for i in range(0, len(third_row)))
    new_board = new_first_row + "\n" + lines_row + \
                "\n" + new_second_row + "\n" + lines_row + \
                "\n" + new_third_row
    return new_board
    
# For troubleshooting and testing purposes
first_row = 'XOX'
second_row = 'OXO'
third_row = 'OOX'   
print(format_tic_tac_toe_board(first_row, second_row, third_row))


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
