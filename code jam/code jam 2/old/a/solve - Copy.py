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

def create_subnodes(node):
	tmp = []
	for x in range(0,len(node.S)-node.W+1):
		if "-" not in node.S[x:x+node.W] and flip(x,S,W) not in known:
			continue
		tmp.append(Node(copy.deepcopy(flip(x,S,W)),node.depth+1, node.W))
	return tmp
	
  
class Node:
	def __init__(self,S,depth,W):
		global known
		self.S = copy.deepcopy(S)
		self.subnodes = []
		self.depth = depth
		self.W = W
		known.append(S)
  
# occupied, ls, rs,
for item in data:
	S = list(item[0])
	W = int(item[1])
	sb= []
	base = Node(S,0,W)
	timer = 0
	current = [base]
	value = 0
	cnt= True
	while(cnt):
		timer += 1
		tmp = []	
		if (timer > 3):
			solutions.append("impossible")
			cnt = False
			break
		for i in current:
			if "-" not in i.S:
				solutions.append(i.depth)
				cnt= False
				break
			tmp += create_subnodes(i)
		current = copy.deepcopy(tmp)
print(known)
	

x = 1		
for item in solutions:
	print("Case #" +str(x)+ ": " +str(item))
	x += 1
	
	
	
	
	
print(flip(4,list("+++++++"),3))