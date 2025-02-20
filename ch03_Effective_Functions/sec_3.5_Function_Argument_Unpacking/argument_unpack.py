
#Unpack function arguments from sequences and dictionaries with the * and ** operators.

def print_vector(x, y, z):
    print(f"<{x}, {y}, {z}>")

#print_vector(0,1,0)

tuple_vec = (1,0,1)
list_vec = [1,0,1]
#print_vector(
#tuple_vec[0],
#tuple_vec[1],
#tuple_vec[2],
#)

#print_vector(*tuple_vec)
#print_vector(*list_vec)

#Puting a * before an iterable in a function call will unpack it and pass its elements as separate positional arguments to the called function.
#This technique works for any iterable, including generator expressions. 
#Using the * operator on a generator consumes all elements from the generator and passes them to the function:
#genexpr = (x * x for x in range(3))
#print_vector(*genexpr)

dict_vec = {'y':0, 'z':1, 'x':1}
print_vector(*dict_vec) # <y, z, x> 
print_vector(**dict_vec) # <1, 0, 1>

#dict_vec2 = {"y":1, "x":0, "u":99.5}
#print_vector(**dict_vec2)
# TypeError: print_vector() got an unexpected keyword argument 'u'
#Because dictionaries are unordered, this matches up dictionary values and function arguments based on the dictionary keys: the x argument receives the value associated with the 'x' key in the dictionary. 

#dict_vec3 = {"x":5, "z":100, }
#print_vector(**dict_vec3)
# TypeError: print_vector() missing 1 required positional argument: 'y'
