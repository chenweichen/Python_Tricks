
from typing import Callable

def strong(func: Callable):
    def wrapper():
        return "<strong>" + func() + "</strong>"
    return wrapper

def emphasis(func):
    def wrapper():
        return "<em>" + func() + "</em>"
    return wrapper


# from bottom to top
@strong
@emphasis
def greet():
    return "hello"




print(f"{greet()}")