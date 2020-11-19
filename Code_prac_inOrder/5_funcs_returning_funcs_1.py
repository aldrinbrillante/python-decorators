# repl.it: https://repl.it/@MakeSchool/FunctionsReturningFunctions2#main.py

def get_speak_func(volume):

    def whisper(text):
        return text.lower() 

    def yell(text):
        return text.upper()

    if volume > 0.5:
        return yell
    else:
        return whisper


speak_func = get_speak_func(0.9)

print(speak_func)
print(speak_func("Hello"))
