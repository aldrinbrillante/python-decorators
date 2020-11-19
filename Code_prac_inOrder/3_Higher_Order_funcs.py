# reply.it: https://repl.it/@MakeSchool/HigherOrderFunctions#main.py


# Two math functions
def summ(num1, num2):
  return num1 + num2

def diff(num1, num2):
  return num1 - num2


# HOF - which accepts func as a parameter
def calculate(math_func):
  answer = math_func(8, 2)
  return answer


result_sum = calculate(summ)
print(result_sum)


result_diff = calculate(diff) 
print(result_diff)

