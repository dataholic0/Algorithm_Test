"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

# Binary search 
"""

import copy

def searchRange(nums, target)->list:

	len_nums = len(nums)
	
	if len_nums == 0:
		return [-1,-1]

	left = 0
	right = len_nums
	mid = 0
	find_index = 0
	
	while left < right:
		mid = (left + right)//2
		
		if abs(right - left) == 1:
			break

		if target > nums[mid]:
			left = mid
		elif target < nums[mid]:
			right = mid
		elif target == nums[mid]:
			find_index = mid
			break
	
	if nums[mid] == target:
		find_index = mid
	else:
		return [-1,-1]

	answer = [find_index, find_index]
	
	while True:
		temp = copy.deepcopy(answer)
		
		if answer[0]-1 >=0 and nums[answer[0]-1] == target:
			answer[0] -= 1
		if answer[1]+1 <= len_nums-1 and nums[answer[1]+1] == target:
			answer[1] += 1
		if temp == answer:
			return answer
		else:

			continue


def best_answer(nums,target):
	def binarySearchLeft(A,x):
		left, right = 0, len(A)-1
		while left <= right:
			mid = (left + right) //2
			if x > A[mid]:
				left = mid + 1
			else:
				right = mid - 1
		return left

	def binarySearchRight(A, x):
		left, right = 0 , len(A) -1
		while left <= right:
			mid = (left+right) //2
			if x >= A[mid]:
				left = mid + 1
			else:
				right = mid - 1
		return right

	left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
	return (left,right) if left <= right else [-1,-1]
