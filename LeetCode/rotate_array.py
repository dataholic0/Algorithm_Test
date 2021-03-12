import copy

def rotate(nums, k):
	
	if len(nums) < k:
		k -= len(nums)

	temp = copy.deepcopy(nums)

	for i in range(len(nums)):
		nums[i] = temp[i-k]

	
nums = [1,2,3,4,5,6,7]
k=3
rotate(nums,k)