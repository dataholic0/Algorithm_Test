from collections import deque

def rustMurderer(n, roads, source):

	# make a other place as a list 
	others = [x for x in range(1, n+1)]
	others.pop(source-1)

	map_dict = {x:[] for x in range(1,n+1)}
	
	for start,end in roads:
		map_dict[start].append(end)
		map_dict[end].append(start)

	answer =[]
	for place in others:
		distance = 0
		queue = deque([source])

		while queue:
			temp_queue = deque()
			distance += 1
			visited = set()
			Finish = False
			for _ in range(len(queue)):
				curr_place = queue.popleft()
				visited.add(curr_place)

				if place in map_dict.get(curr_place):
					temp = list(set(others).difference(map_dict.get(curr_place)).difference(visited))
					temp_queue.extend(temp)
				else:
					answer.append(distance)
					Finish = True
					break
			if Finish:
				break
			else:
				queue = temp_queue
	
	return answer



n = 4
roads = [[1,4],[1,2],[2,3]]
source = 1

rustMurdered(n,roads, source)