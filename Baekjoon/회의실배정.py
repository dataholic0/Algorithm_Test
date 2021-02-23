from collections import deque

def solution(array):
	array = deque(array)
	recent = array.popleft()
	answer = 1

	while array:
		curr = array.popleft()

		if curr[0] >= recent[1]:
			recent = curr
			answer += 1

	return answer





n = int(input())
array = []

for _ in range(n):
	array.append(list(map(int,input().split())))

array.sort(key = lambda x: (x[1],x[0]))

print(solution(array))