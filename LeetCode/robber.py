def rob(nums)->int:

	l = len(nums)

	if l == 0:
		return 0
	elif l <=2:
		return max(nums)

	d = [0]*l
	d[0] = nums[0]
	d[1] = max(nums[0],nums[1])

	for i in range(2, l):
		d[i] = max(d[i-1], d[i-2]+nums[i])
		
	return d[-1]


nums = [2,7,9,3,1]
print(rob(nums))