# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import copy
import math
from pandas import *
import numpy
solutions = []
data = []
cases = int(input())  # read a line with a single integer
for i in range(1, cases + 1):
	n, m = [int(s) for s in input().split(" ")] 
	tmp = [n,m,[]]
	for j in range(1, m + 1):
		tmp[2].append([int(s) for s in input().split(" ")])
	data.append(tmp)	
	
for item in data:
	length=item[0]
	slowest=0
	slowest_time=0
	for horse in item[2]:
		current_time = (length-horse[0])/horse[1]
		if(current_time > slowest_time):
			slowest = item[2].index(horse)
			slowest_time = current_time
	optimum_speed = length/(slowest_time)
	solutions.append(optimum_speed)
	
			

	
			
			
			
			
			
			
			
			
			
			
			
x = 1		
for item in solutions:
	print("Case #" +str(x)+ ": " +str(item))
	x += 1
	
	