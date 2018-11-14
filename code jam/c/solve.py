# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

import math
solutions = []
cases = int(input())  # read a line with a single integer
data = []
stalls = []
for i in range(1, cases + 1):
	data.append([int(s) for s in input().split(" ")] ) 
  
  
  
# occupied, ls, rs,  
for item in data:
	
	space=[item[0]]
	for x in range(item[0]):
		max_value = max(space)
		max_index = space.index(max_value)
		if(max_value%2==0):
			space[max_index] = (max_value/2)-1
			space.insert(max_index,max_value/2)		
		else:
			value = math.floor(max_value/2)
			space[max_index] = value
			space.insert(max_index,max_value-value)
			
	solutions.append([max([space[max_index],space[max_index+1]]),min([space[max_index],space[max_index+1]])])

  


x = 1		
for item in solutions:
	print("Case #" +str(x)+ ": " +str(item[0])+ " " + str(item[1]))
	x += 1