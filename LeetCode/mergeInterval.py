def merge(intervals):
	intervals = sorted(intervals, key = lambda x : (x[0],x[1]))
	answer = [intervals[0]]

	for i in range(1,len(intervals)):
		start, end = intervals[i]
		if start > answer[-1][1]:
			answer.append([start,end])
		else:
			if end <= answer[-1][1]:
				continue
			else:
				answer[-1] = [answer[-1][0],end]
	
	print(answer)
	return answer


intervals = [[1,4],[2,3]]
merge(intervals)