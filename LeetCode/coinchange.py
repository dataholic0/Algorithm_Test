"""
given cons of different denominations and a total amount of money amount.
write a function to compute the fewest number of coins
if cannot make any combination of the coins, return -1

dynamic programming
"""

def coinChange(coins, amount)->int:
	if amount == 0:
		return 0
	if min(coins) > amount:
		return -1

	dp = [-1]*(amount+1)
	dp[0] = 0

	for i in range(1, amount+1):
		temp = []
		for j in coins:
			if i >= j and dp[i-j] != -1:
				temp.append(dp[i-j]+1)
		
		if temp:
			dp[i] = min(temp)

	return dp[-1]
