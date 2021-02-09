from collections import deque

def solution(maze, row_len, col_len):
	
	visited = [[0]*col_len for _ in range(row_len)]

	dx = [0,0,1,-1]
	dy = [1,-1,0,0]

	queue = deque([[0,0]])
	visited[0][0] = 1

	while queue:

		curr_row, curr_col = queue.popleft()

		if curr_row == row_len-1 and curr_col== col_len-1:
			print(visited)
			return visited[curr_row][curr_col]


		for i in range(4):
			nx = curr_row+dx[i]
			ny = curr_col+dy[i]

			if (0<=nx<row_len) and (0<=ny<col_len):
				if (maze[nx][ny] == 1) and (visited[nx][ny] == 0):
					visited[nx][ny] = visited[curr_row][curr_col]+1
					queue.append([nx, ny])




row_len, col_len = map(int, input().split())
maze = []
destination = [row_len, col_len]

for _ in range(row_len):
	maze.append(list(map(int, list(input()))))


print(solution(maze, row_len, col_len))