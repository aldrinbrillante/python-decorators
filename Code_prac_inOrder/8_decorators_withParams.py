# repl.it: https://repl.it/@MakeSchool/DecoratorWithParams#main.py


'''
Currently our Enter and Exit messages are hardcoded as "Entering Function" and "Exiting Function".

Let's make our decorator even more dynamic by allowing the user to pass in what enter and exit message they would like


Entering Function
Hello World / whatever the function did
Exiting Function

'''


# Step one, create a function with the name you want for your decorator (@enter_exit_logging -> enter_exit_logging) and give it parameters, enter_msg and exit_msg


def enter_exit_logging(enter_msg, exit_msg):

  def wrapper(func):
    print(enter_msg)
    func()
    print(exit_msg)

  return wrapper

# Step 2: Inside enter_exit_logging create a wrapper function, it takes one parameter, func (which will be the function you decorate)


# Step 3: Inside your wrapper, write the logic for your decorator.



# Step 4: Outside wrapper(), but inside enter_exit_logging  return the wrapper function.



#Step 5: Let's test.

# Use the @ symbol and the name of the function name of the decorator

@enter_exit_logging("Test enter message", "Test exit message")
def hello_world():
  print("Hi World!")

print(hello_world)
hello_world()

