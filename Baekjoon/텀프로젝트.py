from collections import defaultdict


def solution(n_student, selected_student):
	graph_dict = defaultdict(int)
	visited = [0]*(n_student+1)

	for x,y in enumerate(selected_student, start = 1):
		graph_dict[x] = y

	group = 1

	for start_node in range(1, n_student+1):
		if visited[start_node] == 0:
			while visited[start_node] == 0:
				visited[start_node] = group
				start_node = graph_dict[start_node]
			while visited[start_node] == group:
				visited[start_node] = -1
				start_node = graph_dict[start_node]

			group += 1

	count = 0
	for v in visited:
		if v > 0:
			count += 1
	return count


num_tests = int(input())

for _ in range(num_tests):
	n_student = int(input())
	selected_student = list(map(int, input().split()))
	print(solution(n_student, selected_student))