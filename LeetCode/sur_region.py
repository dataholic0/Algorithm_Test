
import pprint
def solve(board)->None:

	r = len(board)
	c = len(board[0])
	start = set()
	row_can = [0,r-1]
	col_can = [0,c-1]
	visited = [[False]*c for _ in range(r)]
	dx = [0,0,1,-1]
	dy = [1,-1,0,0]

	for i in range(r):
		if board[i][0] == 'O':
			start.add((i,0))
		if board[i][c-1] == 'O':
			start.add((i,c-1))

	for i in range(c):
		if board[0][i] == 'O':
			start.add((0,i))
		if board[r-1][i] == 'O':
			start.add((r-1,i))

	while start:
		cur_r, cur_c = start.pop()
		visited[cur_r][cur_c] = True

		for k in range(4):
			nx = cur_r + dx[k]
			ny = cur_c + dy[k]

			if (0<=nx<=r-1) and (0<=ny<=c-1) and board[nx][ny]=='O' and visited[nx][ny] is False:
				start.add((nx,ny))

	for i in range(r):
		for j in range(c):
			if board[i][j] == 'O' and visited[i][j] == False:
				board[i][j] = 'X'


board = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
solve(board)