#add = lambda x, y: x + y
#print(f"add(2,3): {add(2,3)}")


#print((lambda x, y: x - y)(2,3))

#tuples = [(1, "d"), (2, "b"),(3, "a"),(4, "c")]

#print(sorted(tuples, key=lambda x: x[1]))

#print(sorted(range(-5, 6), key=lambda x: x*x))

def make_adder(n):
    return lambda x: x + n

plus_3 = make_adder(3)
plus_5 = make_adder(5)

print(f"{plus_3(4)}")

print(f"{plus_5(6)}")
# In the above example, the x + n lambda can still access the value of n even though it was defined in the make_adder function(the enclosing scope).

# Sometimgs, using a lambda function instead of a nested function declared with the def keyword can express the programmer's intent more clearly. But to be jonest, this isn't a common occurence-at least not in the kind of code that I like to write. So let's talk a little more about that.

