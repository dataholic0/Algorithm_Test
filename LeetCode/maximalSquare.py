def maximalSquare(matrix)->int:
	if matrix is None or len(matrix) < 1:
		return 0

	max_area = 0
	len_row, len_col = len(matrix), len(matrix[0])

	dp = [[0]*(len_col+1) for _ in range(len_row+1)]

	for i in range(len_row):
		for j in range(len_col):
			if matrix[i][j] == '1':
				dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1])+1
			max_area = max(max_area, dp[i+1][j+1])

	return max_area**2


matrix =  [["0","0","0","0","0"],["1","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"]]
print(maximalSquare(matrix))



"""
reference:
https://leetcode.com/problems/maximal-square/discuss/600149/Python-Thinking-Process-Diagrams-DP-Approach
"""