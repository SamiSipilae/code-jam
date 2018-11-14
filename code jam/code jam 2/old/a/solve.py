# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import copy
import math
solutions = []
cases = int(input())  # read a line with a single integer
data = []
known = []
for i in range(1, cases + 1):
	data.append([s for s in input().split(" ")] ) 
	
	
def flip(x,l,W):
	S = copy.deepcopy(l)
	for y in range(int(W)):
		if S[x+y] == "-":
			S[x+y] = "+"
		else:
			S[x+y] = "-"
	return S


# occupied, ls, rs,
for item in data:
	known = []
	S = list(item[0])
	W = int(item[1])
	strings= [[S,0]]
	known.append(S)
	timer = 0
	cont = True
	while(cont):
		tmplist = []
		timer += 1
		for item in strings:
			if "-" not in item[0]:
				solutions.append(item[1])
				cont = False
				break
		if (cont == False):
			break
		if (timer > 10000):
			solutions.append("IMPOSSIBLE")
			break
		for candidate in strings:
			for x in range(0, len(candidate[0])-W+1):
				if "-" in candidate[0][x:W+x]:
					newstring = flip(x,candidate[0],W)
					if newstring not in known:
						#print(*newstring, sep='')
						known.append(newstring)
						tmplist.append([newstring,candidate[1]+1])
			strings.remove(candidate)
		strings = tmplist
		if(len(strings)) == 0:
			solutions.append("IMPOSSIBLE")
			cont = False
			break	


x = 1		
for item in solutions:
	print("Case #" +str(x)+ ": " +str(item))
	x += 1
	
	