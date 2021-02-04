def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    
    # To use Count sort, we count each number using dict
    count_dict = {x:0 for x in range(3)}
    
    for i in nums:
        count_dict[i] += 1
    
    # we should modify the nums itself. so we have to iterate nums and change one by one
    j = 0
    for i in range(3):
        count = count_dict[i]
        
        while count:
            
            nums[j] = i
            j += 1
            count -= 1