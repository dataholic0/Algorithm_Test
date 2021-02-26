from collections import Counter

def longestSubstring(s,k)->int:

	# Recursive end condition
	if len(s) == 0 or k > len(s):
		return 0

	count_dict = Counter(s)
	s1,s2 = "",""

	for index,letter in enumerate(s):
		if count_dict[letter] < k:
			s1 = longestSubstring(s[:index],k)
			s2 = longestSubstring(s[index+1],k)
			break
	
	# else condition here stands for all characters in s is over 3
	else:
		return len(s)

	return max(s1,s2)


	
	


s = 'ababacb'
k = 3
print(longestSubstring(s,k))