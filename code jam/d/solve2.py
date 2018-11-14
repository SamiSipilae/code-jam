# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import copy
import math
from pandas import *
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
	
def check_rows(matrix):
	tmp = 0
	for x in range(len(matrix)):
		for y in range(len(matrix[0])):
			for j in range(len(matrix[0])):
				if(obj[0][x][j] == "o" or obj[0][x][j] == "x" ):
					tmp += 1
				if(obj[0][j][y] == "o" or obj[0][x][j] == "x" ):
					tmp += 1
	return tmp

	
for item in data:
	candidates = []
	known = []
	field = [[0]*item[0] for i in range(item[0])]
	for model in item[2]:
		field[int(model[1])-1][int(model[2])-1] = model[0]
	candidates.append([field,[]])
	cnt= True
	while(cnt):
		for obj in candidates:
			new_candidates= []
			for x in range(len(obj[0])):
				for y in range(len(obj[0])):
					can_place= ["o",'+',"x"]
					if(obj[0][x][y] == 'o'):
						continue
					tmp = 0
					for j in range(len(obj[0])):
						if(obj[0][x][j] == "o" or obj[0][x][j] == "x" ):
							tmp += 1
						if(obj[0][j][y] == "o" or obj[0][x][j] == "x" ):
							tmp += 1
					if(tmp>0):
						if("o" in can_place):
							can_place.remove("o")
						if("x" in can_place):
							can_place.remove("x")
					tmp = 0
					for k in range(0,len(obj[0])):
						if(x+k<len(obj[0]) and y+k <len(obj[0])):
							if(obj[0][x+k][y+k] == "o" or obj[0][x+k][y+k] == "+" ):
								tmp += 1
						if(x-k>-1 and y-k >-1):
							if(obj[0][x-k][y-k] == "o" or obj[0][x-k][y-k] == "+" ):
								tmp += 1
						if(x+k<len(obj[0]) and y-k >-1):
							if(obj[0][x+k][y-k] == "o" or obj[0][x+k][y-k] == "+" ):
								tmp += 1
						if(x-k>-1 and y+k<len(obj[0])):
							if(obj[0][x-k][y+k] == "o" or obj[0][x-k][y+k] == "+" ):
								tmp += 1
					if(tmp>0):
						if("o" in can_place):
							can_place.remove("o")
						if("+" in can_place):
							can_place.remove("+")
							
					for item in can_place:
						tmp_copy = copy.deepcopy(obj)
						print(DataFrame(tmp_copy[0]).to_string(index=False))
						print(1)
						tmp_copy[0][x][y] = item
						if(tmp_copy[0] not in known):
							known.append(tmp_copy[0])
							tmp_copy[1].append([item,x,y])
							new_candidates.append(tmp_copy)
			
						
						
		if(len(new_candidates) >0):
			candidates = new_candidates
		else:
			best = 0
			score = 0
			tmp_score = 0
			for obj in candidates:
				tmp_score = 0
				for x in range(len(obj[0])):
					for y in range(len(obj[0][x])):
						if(obj[0][x][y] == "o"):
							tmp_score+= 2
						if(obj[0][x][y] == "x" or obj[0][x][y] == "+"):
							tmp_score+= 1
				if(score < tmp_score):
					best=obj
					score = tmp_score
			#print(DataFrame(best[0]))
			solutions.append([score,best[1]])
			cnt=False
x = 1		
for item in solutions:
	print("Case #" +str(x)+ ": " +str(item[0]) + " " + str(len(item[1])))
	for line in item[1]:
		print(line[0] + " " + str(line[1]) + " " + str(line[2]))
	
	x += 1
	
	