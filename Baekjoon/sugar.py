def solution(weight):

	answer = [0,-1,-1]

	for i in range(3, weight+1):

		if i>=5 and answer[i-5] != -1:
			answer.append(1+answer[i-5])
		elif answer[i-3] != -1:
			answer.append(1+answer[i-3])
		else:
			answer.append(-1)

	return answer[-1]

weight = int(input())

print(solution(weight))