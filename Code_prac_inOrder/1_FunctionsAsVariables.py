# repl.it: https://repl.it/@MakeSchool/FunctionsAsVariables#main.py

def greet(name):
  return f"Hello, {name}"


print(greet("Joi"))

print("greet prints as:", greet)

say_hello = greet 
print("say_hello prints as:",say_hello)

# say_hello("David")
