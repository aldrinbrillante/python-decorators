# repl.it: https://repl.it/@MakeSchool/NestedFunctions#main.py

def print_msg(msg):
    # This is the outer enclosing function
    print("I am in the outer function")
    
    def printer(txt):
        # This is the nested function
        print("I am in the nested function")
        print(txt)

    printer(msg)



print_msg("Hello")

#The code below will throw an error. Read the error.
#printer("Hello")