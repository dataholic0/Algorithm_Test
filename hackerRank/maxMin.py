def maxMin(k, arr):

	arr.sort()
	answer = float('inf')

	for i in range(len(arr)-k+1):
		answer = min(answer, arr[i+k-1]- arr[i])

	return answer
