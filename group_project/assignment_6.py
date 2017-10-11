
BOARD_TEMPLATE = """
{0}  |  {1}  |  {2}
--------------
{3}  |  {4}  |  {5}
--------------
{6}  |  {7}  |  {8}
"""

   
    
def format_tic_tac_toe_board(first_row, second_row, third_row):
    r1 = list(first_row)
    r2 = list(second_row)
    r3 = list(third_row)    

    return(BOARD_TEMPLATE.format(r1[0], r1[1], r1[2], r2[0], r2[1], r2[2], r3[0], r3[1], r3[2]))
    

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
