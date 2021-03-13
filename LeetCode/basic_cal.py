from collections import deque

def calculator(s)->str:
	s = s.replace(' ','')
	s = s.replace('/', '//')

	answer = eval(s)
	return answer
	
s = "1+3+5/2+5/2"
print(calculator(s))


# 1+3-2/2*4+1/5