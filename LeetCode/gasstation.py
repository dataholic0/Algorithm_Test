"""
given two integer gas and cost, return the starting gas station's index if can travel, else return -1
"""


def canCompleteCircuit(gas,cost)->int:
	sub = [x-y for x,y in zip(gas,cost)]
	start_index = []
	l = len(gas)

	if sum(sub) < 0:
		return -1

	for index, value in enumerate(sub):
			start_index.append(index)

	for index in start_index:
		temp = 0
		for i in range(index, index+l):
			if i < l:
				temp += sub[i]
			else:
				temp += sub[i-l]

			if temp <0:
				break
		else:
			return index
	else:
		return False

gas = [2,3,4]
cost = [3,4,3]
print(canCompleteCircuit(gas,cost))