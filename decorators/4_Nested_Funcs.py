# repl.it: https://repl.it/@MakeSchool/NestedFunctions#main.py
def print_msg(msg):
    # This is the outer enclosing function
    print("I am in the outer function")
    
    def printer(txt):
        # This is the nested function
        print("I am in the nested function")
        print(txt)

    printer(msg)



# print_msg("Hello")

#The code below will throw an error. Read the error.
# printer("Hello")



# def weather(temp):

#   def say_weather(t):
#     print(f"Today's temp is: {t}")



def weather(90):

  def say_weather(t):
    # prints todays temperature
    print(f"today's temp is {t}")

  def say_goodnight():
    print("Good night!")

  say_weather(90)

  say_goodnight()

weather(90)
