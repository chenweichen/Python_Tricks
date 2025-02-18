def null_decorator(func):
    return func

def greet():
    return "Hello"

greet = null_decorator(greet)
print(greet())



def null_decorator2(func):
    return func

@null_decorator2
def greet2():
    return "hahaha"

print(greet2())

