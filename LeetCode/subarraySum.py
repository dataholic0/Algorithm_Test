from collections import deque
from itertools import combinations

def subarraySum(nums,k)->int:
	"""
	return the total number of continuous subarrays whose sum equals to k
	"""
	sum_list = [0]
	answer = 0

	for i in range(len(nums)):
		sum_list.append(sum_list[-1]+nums[i])

	print(sum_list)


nums = [1,1,1]
k = 2
subarraySum(nums,k)