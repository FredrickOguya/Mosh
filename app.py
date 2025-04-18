message = "a"

def greet(name):
    global message
    message = "b"



greet("mosh")
print(message)