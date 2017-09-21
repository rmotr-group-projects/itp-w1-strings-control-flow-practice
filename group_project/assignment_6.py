# Example. Use it as a base to build your own template.
BOARD_TEMPLATE = """
O  |  O  |  X
--------------
X  |  X  |  O
--------------
O  |  X  |  O
"""


def format_tic_tac_toe_board(first_row, second_row, third_row):
  appends_columns = '  |  '
  horizontal_spacer = '--------------'
  first_rowc1 = first_row [0]
  first_rowc2 = first_row [1]
  first_rowc3 = first_row [2]
  row1 = first_rowc1 + appends_columns + first_rowc2 + appends_columns + first_rowc3
  str_row1 = str(row1)
  second_rowc1 = second_row [0]
  second_rowc2 = second_row [1]
  second_rowc3 = second_row [2]
  row2 = second_rowc1 + appends_columns + second_rowc2 + appends_columns + second_rowc3
  str_row2 = str(row2)
  third_rowc1 = third_row [0]
  third_rowc2 = third_row [1]
  third_rowc3 = third_row [2]
  row3 = third_rowc1 + appends_columns + third_rowc2 + appends_columns + third_rowc3
  str_row3 = str(row3)
  return str('\n' + str_row1 + '\n' + horizontal_spacer + '\n' + str_row2 + '\n' + horizontal_spacer + '\n' + str_row3 +'\n'+'\n')

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
