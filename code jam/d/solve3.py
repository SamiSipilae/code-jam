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
		tmp[2].append([s for s in input().split(" ")])
	data.append(tmp)	
	
	
	#print(DataFrame(tmp_copy[0]))
	
def check_rows(matrix,x,y):
	tmp = 0
	for j in range(0,len(matrix[0])):
		if(matrix[x][j] == "o" or matrix[x][j] == "x" ):
			#print(str(x)+","+str(j)+"="+str(matrix[x][j]))
			tmp += 1
		if(matrix[j][y] == "o" or matrix[j][y] == "x" ):
			#print(str(j)+","+str(y)+"="+str(matrix[x][j]))
			tmp += 1
	return tmp

def check_diagonals(matrix,x,y):
	tmp = 0
	for k in range(1,len(matrix[0])):
		if(x+k<len(matrix[0]) and y+k <len(matrix[0])):
			if(matrix[x+k][y+k] == "o" or matrix[x+k][y+k] == "+" ):
				tmp += 1
		if(x-k>-1 and y-k >-1):
			if(matrix[x-k][y-k] == "o" or matrix[x-k][y-k] == "+" ):
				tmp += 1
		if(x+k<len(matrix[0]) and y-k >-1):
			if(matrix[x+k][y-k] == "o" or matrix[x+k][y-k] == "+" ):
				tmp += 1
		if(x-k>-1 and y+k<len(matrix[0])):
			if(matrix[x-k][y+k] == "o" or matrix[x-k][y+k] == "+" ):
				tmp += 1
	return tmp
	
	
def can_place_o(M,x,y):
	if(check_rows(field,x,y) >0):
		return False
	if(check_diagonals(field,x,y)>0):
		return False
	return True

def can_place_x(M,x,y):
	if(check_rows(field,x,y) >0):
		return False
	return True	

def can_place_plus(M,x,y):
	if(check_diagonals(field,x,y) >0):
		return False
	return True	
	
	
for item in data:
	candidates = []
	potential_moves = []
	known = []
	field = [[0]*item[0] for i in range(item[0])]
	for model in item[2]:
		field[int(model[1])-1][int(model[2])-1] = model[0]
	cnt= True
	timer =0
	moves = []
	while(timer < 20):
		timer +=1
		for x in range(len(field)):
			for y in range(len(field)):
				if(field[x][y] != 0):
					continue
				if(can_place_o(field,x,y)):
						field[x][y] = "o"
						moves.append(["o",x,y])
				elif(can_place_x(field,x,y)):
						field[x][y] = "x"
						moves.append(["x",x,y])
				elif(can_place_plus(field,x,y)):
						field[x][y] = "+"
						moves.append(["+",x,y])
	while(timer < 20):
		timer +=1
		for x in range(len(field)):
			for y in range(len(field)):
				if(field[x][y] == 0):
					continue
				if(can_place_o(field,x,y)):
						field[x][y] = "o"
						moves.append(["o",x,y])

	
		
	print(1)
	tmp_score = 0
	print(DataFrame(field))
	for x in range(len(field)):
		for y in range(len(field[x])):
			if(field[x][y] == "o"):
				tmp_score+= 2
			if(field[x][y] == "x" or field[x][y] == "+"):
				tmp_score+= 1
		score = tmp_score
	solutions.append([score,moves])
			
			
			
			
			
			
			
			
			
			
			
			
			
			
x = 1		
for item in solutions:
	print("Case #" +str(x)+ ": " +str(item[0]) + " " + str(len(item[1])))
	for line in item[1]:
		print(line[0] + " " + str(line[1]+1) + " " + str(line[2]+1))
	
	x += 1
	
	