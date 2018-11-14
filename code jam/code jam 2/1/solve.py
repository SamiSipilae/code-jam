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
	for j in range(1, n + 1):
		tmp[2].append([int(s) for s in input().split(" ")])
	data.append(tmp)	
	

def find_largest(list):
	cur=0
	val=0
	for item in list:
		area = 2*math.pi*item[0]**2 +2*math.pi*item[0]*item[1]
		print(item)
		print(area)
		if area>val:
			val = area
			cur =list.index(item)
	return cur
	
def find_thickest(list):
	cur=0
	val=0
	for item in list:
		if item[1]>val:
			val = item[1]
			cur =list.index(item)
	return cur	

def find_widest(list):
	cur=0
	val=0
	for item in list:
		if item[0]>val:
			val = item[0]
			cur =list.index(item)
	return cur	


	
for item in data:
	pancakelist = item[2]
	largestlist = []
	for x in range(item[1]):
		largest =find_largest(pancakelist)
		largestlist.append(pancakelist[largest])
		pancakelist.remove(pancakelist[largest])
	print(largestlist)
	largest = find_widest(largestlist)
	area = math.pi*largestlist[largest][0]**2
	area += 2*math.pi*largestlist[largest][0]*largestlist[largest][1]
	item[1] -= 1
	largestlist.remove(largestlist[largest])
	while( item[1] >0):
		thickest = find_thickest(largestlist)
		area +=  2*math.pi*largestlist[thickest][0]*largestlist[thickest][1]
		largestlist.remove(largestlist[thickest])
		item[1] -= 1
	solutions.append(area)
			
x = 1		
for item in solutions:
	print("Case #" +str(x)+ ": "+ str(item) )
	x += 1
	
	