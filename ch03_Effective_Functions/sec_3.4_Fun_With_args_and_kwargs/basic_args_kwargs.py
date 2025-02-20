
from ast import arguments


def foo(required, *args, **kwargs):
    print(f"required: {required}\n")
    if args:
        print(f"args: {args}\n")
    if kwargs:
        print(f"kwargs: {kwargs}\n")


#The above function requires at least one argument called "required," 
#but it can accept extra positional and keyword arguments as well.

#If we call the function with additional arguments, 
#args will collect extra positional arguments as a tuple 
#because the parameter anme has a * prefix. 

#Likewise, kwargs will collect extra keyword arguments as a dictionary 
#because the parameter name has a ** prefix.

#Both args and kwargs can be empty 
#if no extra arguments are passed to the functin.else

#As we call the function with various combinations of arguments, 
#you'll see how Python collects them inside the args and kwargs parameters 
#according to whether hey're positional or keyword argements:

#foo()
# TypeError: foo() missing 1 required positional argument: 'required'


#foo('hello')
# required: hello
#*args collect extra positonal arguments as a tuple 
#**kwargs collect extra keyword arguments as a dictionary 

#foo("hwllo", 1,2,3)
#required: hwllo
#args: (1, 2, 3)

#foo("hello", 1,2, key1="value1", key2 = 999)
#required: hello
#args: (1, 2)
#kwargs: {'key1': 'value1', 'key2': 999

def goo(required, *args, **kwargs):
    print(f"required: {required}; type: {type(required)}")
    if args:
        print(f"args: {args};type: {type(args)}")
    if kwargs:
        print(f"kwrargs: {kwargs}; type{type(kwargs)}")

#goo('world')
# required: world; type: <class 'str'>

#goo("hi", 2,4,6)
#required: hi; type: <class 'str'>
#args: (2, 4, 6);type: <class 'tuple'>

#goo("hi", 1,3, ost="foo", fyi=987.6)
#required: hi; type: <class 'str'>
#args: (1, 3);type: <class 'tuple'>
#kwrargs: {'ost': 'foo', 'fyi': 987.6}; type<class 'dict'>

#goo("got your back", key=123, value="789")
#required: got your back; type: <class 'str'>
#kwrargs: {'key': 123, 'value': '789'}; type<class 'dict'>

# Modify the arguments before you pass them along.

def foo(x, *args, **kwargs):
    kwargs['name'] = "Alice"
    new_args = args + ('extra', )
    print(f"new_args: {new_args}\n")
    print(f"kwargs: {kwargs}")

#foo(66, 33, title="wonderland")
#new_args: (33, 'extra')
#kwargs: {'title': 'wonderland', 'name': 'Alice'}
