import string
from itertools import product
from functools import reduce

def letterCombinations(digits):
	if len(digits) == 0:
		return ''

	convert_dict = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
	convert = list(map(lambda x: list(convert_dict[x]), list(map(int, list(digits)))))
	answer = [reduce(lambda a,b: a+b, x) for x in list(product(*convert))]

	return answer



digits = '7'

letterCombinations(digits)