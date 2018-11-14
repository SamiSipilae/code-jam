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
	prev_room = 0
	space=item[0]
	target=item[1]
	room = 0
	while(True):
		
		next_step = space/2  
		if target > next_step:
			solutions.append([room, prev_room])
			break
		else:
			space=next_step
			prev_room=room
			room =+1 
			

  


x = 1		
for item in solutions:
	print("Case #" +str(x)+ ": " +str(item[0])+ " " + str(item[1]))
	x += 1