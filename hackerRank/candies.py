def candies(n,arr):
	answer = [1]*n

	for i in range(1,n):
		if arr[i] > arr[i-1] and answer[i] <= answer[i-1]:
			answer[i] = answer[i-1] + 1
	for i in range(n-2,-1,-1):
		print(i)
		if arr[i] > arr[i+1] and answer[i] <= answer[i+1]:
			answer[i]  = answer[i+1] + 1

	return sum(answer)

n = 10
arr = [2,4,2,6,1,7,8,9,2,1]
print(candies(n,arr))