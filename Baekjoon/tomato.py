col, row = map(int, input().split())
arr = []

for _ in range(row):
	data = list(map(int, input().split()))
	arr.append(data)

def tomatoes(arr):
	
	# Make padding to avoid index error while searching
	temp = [[2]*(len(arr[-1])+2)]
	for i in range(len(arr)):
		temp.append([2] + arr[i] + [2])
	temp.append([2]*(len(arr[-1])+2))
	arr = temp

	answer = 0
	ripe_tomatoes = set() # to avoid duplicate
	unripe_tomatoes_count = 0

	# initial search for finding ripe totmato and unripe totmato
	for row_idx in range(1,len(arr)-1):
		for col_idx in range(1, len(arr[0])-1):
			if arr[row_idx][col_idx] == 1:
				ripe_tomatoes.add((row_idx, col_idx))
			elif arr[row_idx][col_idx] == 0:
				unripe_tomatoes_count += 1

	# bfs with ripe_tomatoes
	while ripe_tomatoes:
		next_turn = set()
		change_count = 0
		
		for row_idx,col_idx in ripe_tomatoes:
				if arr[row_idx-1][col_idx] == 0:
					arr[row_idx-1][col_idx] = 1
					next_turn.add((row_idx-1, col_idx))

				if arr[row_idx+1][col_idx] == 0:
					arr[row_idx+1][col_idx] = 1
					next_turn.add((row_idx+1, col_idx))
					
				if arr[row_idx][col_idx+1] == 0:
					arr[row_idx][col_idx+1] = 1
					next_turn.add((row_idx, col_idx+1))
					
				if arr[row_idx][col_idx-1] == 0:
					arr[row_idx][col_idx-1] = 1
					next_turn.add((row_idx, col_idx-1))
					
		change_count = len(next_turn)
		unripe_tomatoes_count -= change_count
		ripe_tomatoes = next_turn

		if answer == 0 and change_count == 0:
			return 0

		answer += 1

	if unripe_tomatoes_count != 0:
		return -1
	else:
		return answer-1

print(tomatoes(arr))
