# repl.it: https://repl.it/@MakeSchool/uglydecorator#main.py

'''
Components of a Decorator:

1. Take in a function as a parameter

2. Inside that function, define a wrapper function (i.e. a nested function) that uses the passed function and adds stuff to it.

3.Return the wrapper function



#TODO: Write your own ugly decorator that will extend a simpler function by adding "Entering Function" before the function is called and "Exiting Function" after it is called.

Entering Function
Hello World
Exiting Function
'''


# TODO: Create ugly_decorator (you can call it whatever you want btw).

def ugly_decorator(func):

  def wrapper():
    print("Entering Function...")
    func()
    print("Exiting Function...")

  return wrapper

# Note: create our decorator functions before the functions that use it, not after. 


# Our simple function
def hello_world():
    print("Hello World")

#TO DO: After creating your ugly decorator, reassign the original function to the decorated one.

print("Before decorating:")
hello_world()


hello_world = ugly_decorator(hello_world)
print('------------')

print("After decorating:")
hello_world()


def say_goodbye():
  print("See ya!")
print('------------')
say_goodbye = ugly_decorator(say_goodbye)
say_goodbye()