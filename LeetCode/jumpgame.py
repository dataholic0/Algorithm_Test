"""
nums: non-negative integers
"""
def canJump(nums:list)->bool:
	start = 0
	end = len(nums)-1
	if start == end:
		return True

	stack = set([start])
	visited = [0]*(end+1)
	visited[0] = 1

	while stack:		
		curr_idx = stack.pop()
		can_jump = nums[curr_idx]

		temp_max = 0
		max_index = 0

		for i in range(can_jump+1):
			if (curr_idx+i <= end) and (curr_idx+i+nums[curr_idx+i] > temp_max):
				max_index = curr_idx+i
				temp_max = curr_idx+i+nums[curr_idx+i]

		if temp_max >= end:
			return True
		elif visited[max_index] == 0:
			visited[max_index] = 1
			stack.add(max_index)
		else:
			return False


nums = [2,0,0]
print(canJump(nums))