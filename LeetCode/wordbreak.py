"""
given non-empty string and dictionary cotaining a list of non-empty words and no duplicates
"""
from collections import defaultdict

def wordBreak(s,wordDict)->str:
	word_dict = defaultdict(list)

	for word in wordDict:
		word_dict[word[0]].append(word)
	
	for key,value in word_dict.items():
		word_dict[key] = sorted(value, key = lambda x: len(x), reverse = True)

	check = set([s])

	while check:
		
		for i in range(len(check)):
			curr_word = check.pop()

			for j in word_dict.get(curr_word[0], []):
				length = len(j)

				if j == curr_word[:length]:
					if curr_word[length:] == '':
						return True
					else:
						check.add(curr_word[length:])

	else:
		return False






s = "leetcode"
wordDict = ["leet", "code"]

print(wordBreak(s,wordDict))