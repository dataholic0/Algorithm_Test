
# Using dynamic Programming
from math import ceil, sqrt

def numSquares2(n):

	answer = [0,1,2,3]

	for num in range(4,n+1):
		answer.append(num)

		for i in range(1, int(ceil(sqrt(num)))+1):
			temp = i*i
			if temp> i:
				break
			else:
				answer[num] = min(answer[num], 1+answer[num-temp])

	return answer[-1]