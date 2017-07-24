# Example. Use it as a base to build your own template.
BOARD_TEMPLATE = """
O  |  O  |  X
--------------
X  |  X  |  O
--------------
O  |  X  |  O
"""



def format_tic_tac_toe_board(first_row, second_row, third_row):
    fr1 = first_row[0]
    fr2 = first_row[1]
    fr3 = first_row[2]
    sr1 = second_row[0]
    sr2 = second_row[1]
    sr3 = second_row[2]
    tr1 = third_row[0]
    tr2 = third_row[1]
    tr3 = third_row[2]
    return """
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
""".format(fr1,fr2,fr3,sr1,sr2,sr3,tr1,tr2,tr3)



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
