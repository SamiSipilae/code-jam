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
	tmp = []
	tmp.append([int(s) for s in input().split(" ")])
	data.append(tmp[0])	
	
def next(R,Y,B,prev):
	if (R+Y+B) < 0:
		return ""
	if prev == "R":
		if Y>B:
			return "Y"
		else:
			return "B"
	if prev == "B":
		if Y>R:
			return "Y"
		else:
			return "R"
	if prev == "Y":
		if R>B:
			return "R"
		else:
			return "B"	
	if prev == "":
		if R>Y and R >B:	
			return "R"
		elif Y>B:
			return "Y"
		else:
			return "B"
	return
	
for item in data:
	fail = False
	total = item[0]
	R =item[1]
	Y = item[3]
	B = item[5]		
	solution = []
	last = ""
	first = next(R,Y,B,"")
	if first == "R":
		R -= 1
	elif first =="B":
		B -= 1
	else:
		Y -= 1
	solution.append(first)
	last = next(R,Y,B,first)
	if last == "R":
		R -= 1
	elif last =="B":
		B -= 1
	elif last =="Y":
		Y -= 1
	else: 
		fail = True
	
	
	while(not fail):
		if R == 0 and B == 0 and Y == 0:
			break
		tmp = next(R,Y,B,solution[-1])
		if tmp == "R":
			solution.append("R")
			R -= 1
		elif tmp == "Y":
			solution.append("Y")
			Y -= 1			
		elif tmp == "B":
			solution.append("B")
			B -= 1
		else:
			fail = True
			break
			
	if (fail == True):
		solutions.append("IMPOSSIBLE")
	else:
		solution.append(last)
		solutions.append(solution)
			
			
			
			
x = 1		
for item in solutions:
	print("Case #" +str(x)+ ": "+"".join(str(x) for x in item))
	x += 1
	
	