def setZeros(matrix):
	row_l = len(matrix)
	col_l = len(matrix[0])
	
	zero_col = [False]*col_l
	zero_row = [False]*row_l

	for i in range(row_l):
		if 0 in matrix[i]:
			zero_row[i] = True
	
	trans_matrix = [x for x in zip(*matrix)]

	for j in range(col_l):
		if 0 in trans_matrix[j]:
			zero_col[j] = True

	# row Modification
	for i in range(row_l):
		if zero_row[i]:
			matrix[i] = [0]*col_l

	# col modification
	for j in range(col_l):
		if zero_col[j]:
			for k in range(row_l):
				matrix[k][j] = 0

	print(matrix)


matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeros(matrix)