#used summ instead of sum, bc sum is reseved.
def summ(num1, num2):
  return num1 + num2

def diff(num1, num2):
  return num1 - num2

def mult(num1, num2):
  return num1 * num2

funcs = [summ, diff, mult]

for func in funcs:
	print(func(8, 2))

############################
# funcs[0] # sum
# funcs[1] # diff 
# funcs [3] # mult
############################ 

 
# print(funcs[1])
print(funcs[1] (10, 12))