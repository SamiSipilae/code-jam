# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
solutions = []
cases = int(input())  # read a line with a single integer
data = []
stalls = []
for i in range(1, cases + 1):
	data.append([int(s) for s in input().split(" ")] ) 
  
  
def next_stall():
	ls = []
	rs = []
	minlr = []
	maxlr = []
	for item in stalls:
		ls.append(item[1])
		rs.append(item[2])
	for x in range(len(ls)):
		if ls[x] >= rs[x]:
			minlr.append(rs[x])
		else:
			minlr.append(ls[x])
	max_value = max(minlr)
	indexes = [i for i, j in enumerate(minlr) if j == max_value]
	if len(indexes) == 1:
		return indexes[0]
	for x in indexes:
		maxlr.append(max([ls[x],rs[x]]))
	max_value2 = max(maxlr)
	indexes2 = [i for i, j in enumerate(maxlr) if j == max_value2]
	return indexes[min(indexes2)]
	

def update_stalls(ns, person):
	stalls[ns][0] = person
	stalls[ns][1] = 0
	stalls[ns][2] = 0
	x=0
	while(True):
		x += 1
		if (stalls[ns+x][0]!= 0):
			break
		stalls[ns+x][1] = x-1
	x=0
	while(True):
		x -= 1
		if (stalls[ns+x][0]!= 0):
			break
		stalls[ns+x][2] = abs(x)-1
  
  
# occupied, ls, rs,  
for item in data:
	stalls = [[-1,0,0]] + [[0,0,0] for x in range(item[0])]+[[-1,0,0]]
	for index in range(len(stalls)):
		if(index>0):
			if(stalls[index-1][0] == 0 and stalls[index][0] == 0):
				a= 1
				b=index-2
				while(True):
					if(stalls[b][0] == 0):
						a += 1
						b -= 1
					else:
						break
				stalls[index][1] = a
			else:
				stalls[index][1] = 0
		if(index<len(stalls)-1):
			if(stalls[index+1][0] == 0 and stalls[index][0] == 0):
				a= 1
				b=index+2
				while(True):
					if(stalls[b][0] == 0):
						a += 1
						b += 1
					else:
						break
				stalls[index][2] = a
			else:
				stalls[index][2] = 0
	
	for person in range(1, item[1]+1):
		ns = next_stall()	
		if (person < item[1]):
			update_stalls(ns,person)		
		else:
			solutions.append([max([stalls[ns][1],stalls[ns][2]]),min([stalls[ns][1],stalls[ns][2]])])
			


  
  

x = 1		
for item in solutions:
	print("Case #" +str(x)+ ": " +str(item[0])+ " " + str(item[1]))
	x += 1