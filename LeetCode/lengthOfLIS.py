class Solution:
    def lengthOfLIS1(self, nums: List[int]) -> int:
        n = len(nums)

        if nums == sorted(nums, reverse = True):
            return 1
        
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    
        return max(dp)


"""
Below answer is the one of the best answer for this problem
Use Binary Search algorithm, patient sorting concept
reference: https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
"""
"""
    def lengthOfLIS2(self, nums):
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i != j:
            m = (i + j) / 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    return size

"""