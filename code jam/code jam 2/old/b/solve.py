# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
cases = int(input())  # read a line with a single integer
max_num = []
for i in range(1, cases + 1):
  max_num.append(int(input())) 
  
  
  
  
def check(num):
	lst = str(num)
	for x in  range(1,len(lst)):
		if (int(lst[x]) < int(lst[x-1]))	:
			return True
	return False
		  
  
  
solutions = []
for num in max_num:
	while(check(num)):
		digits = str(num)
		if(digits[-1] == "0"):
			num -= 1
		for x in range(1,len(digits)):
			if (digits[x]<digits[x-1]):
				num -= int(digits[x:])
				break
				
				
	solutions.append(num)
		
			
			
			

x = 1		
for item in solutions:
	print("Case #" +str(x)+ ": " +str(item))
	x += 1