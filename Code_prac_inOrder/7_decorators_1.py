# repl.it: https://repl.it/@MakeSchool/decorators#main.py 


# # Our ugly decorator
# def ugly_decorator(func):
#     def wrapper():  
#         print("Entering Function")
#         func()
#         print("Exiting Function")
# return wrapper


# Our simple function
# def hello_world():
#     print("Hello World")



# The ugly way to decorate
hello_world = ugly_decorator(hello_world)
hello_world()



# ✋🏽️ Comment the above code. Uncomment code below.


# The clean way to decorate: 


def ugly_decorator(func):

  def wrapper(): 
    print("Entering Function")
    func()
    print("Exiting Function")

  return wrapper

# Use the @ symbol and the name of the function name of the decorator
@ugly_decorator
def hello_world():
    print("Hello World")

@ugly_decorator
def say_goodbye():
  print("See ya!")

#Now every time we call our decorated function Python knows to also call the extended code in the decorator

hello_world()

say_goodbye()
