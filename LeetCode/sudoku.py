from collections import Counter
def isValidSudoku(board):

	# check the first rule: no duplicate in each row
	for row in board:
		check_row = sorted(Counter(row).values(), reverse= True)
		if len(check_row) > 1 and check_row[1] != 1:
			return False

	# check the second rule: no duplicate in each col
	for col in zip(*board):
		check_col = sorted(Counter(col).values(), reverse= True)
		if len(check_col) > 1 and check_col[1] != 1:
			return False

	# check the third rule: no duplicate in 3*3

	row_can = [0,3,6]
	col_can = [0,3,6]

	for row in row_can:
		for col in col_can:
			exist_num = []
			for curr_row in range(row, row+3):
				for curr_col in range(col, col+3):
					curr_pos = board[curr_row][curr_col]
					if (curr_pos != '.') and (curr_pos not in exist_num):
						exist_num.append(curr_pos)
					elif curr_pos in exist_num:
						return False

	return True