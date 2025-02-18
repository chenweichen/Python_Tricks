
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet():
    return 'hello'

#print(greet())

def null_decorator(func):
    return func


print(f"{greet}\n")
print(f"{null_decorator(greet)}\n")
print(f"{uppercase(greet)}\n")
