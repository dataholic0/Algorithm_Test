
def reverseString(s)->None:
	
	temp = ''
	for i in range(len(s)//2):
		temp = s[i]
		s[i] = s[-(i+1)]
		s[-(i+1)] = temp


s =["h","e","l","l","o"]
reverseString(s)