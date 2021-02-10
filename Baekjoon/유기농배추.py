from collections import deque

def solution(grid):
	num_island = 0
	row_length = len(grid)
	col_length = len(grid[0])

	dx = [0,0,-1,1]
	dy = [1,-1,0,0]

	for row in range(row_length):
		for col in range(col_length):
			if grid[row][col] == '1':
				num_island += 1
				queue = deque([[row,col]])
				grid[row][col] = '0'

				while queue:
					cur_row, cur_col = queue.popleft()

					for i in range(4):
						n_row = cur_row + dx[i]
						n_col = cur_col + dy[i]

						if 0<=n_row<row_length and 0<=n_col<col_length:
							if grid[n_row][n_col] == '1':
								queue.append([n_row, n_col])
								grid[n_row][n_col] = '0'
	return num_island

n_test = int(input())

for _ in range(n_test):
	n_row,n_col,n_let = list(map(int, input().split()))
	land = [['0']*n_col for _ in range(n_row)]
	for _ in range(n_let):
		row_index,col_index = list(map(int, input().split()))
		land[row_index][col_index] = '1'

	print(solution(land))
