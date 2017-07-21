# Example. Use it as a base to build your own template.
BOARD_TEMPLATE = """
{A}  |  {B}  |  {C}
--------------
{D}  |  {E}  |  {F}
--------------
{G}  |  {H}  |  {I}
"""



def format_tic_tac_toe_board(first_row, second_row, third_row):
    new_board = BOARD_TEMPLATE.format(A = first_row[0],B=first_row[1], C = first_row[2], D = second_row[0],E = second_row[1], F = second_row[2], G = third_row[0], H = third_row[1], I = third_row[2])
    return new_board

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
