

#SECTION - Counting upwarts in Python
#numbers = [1,2,3,4,5,6,7,8,9,10]
#for n in numbers:
#    print(f"n: {n}")

#for n in range(1, 11):
#    print(f"n: {n}")

# The range function counts upward starting from that start number, and it stops just before that stop number.
# So we're stopping at 10 here instead of going all the way to 11.

#for i in range(5):
#    print(f"i: {i}")

# When range is give one argument, it starts at 0, and it stops just before that argument.

#!SECTION


#SECTION - Using range with a step value

#for n in range(0, 51, 10):
#    print(f"n: {n}")

#!SECTION


#SECTION - Counting backwards in Python

#for n in range(10, 0, -1):
#    print(f"n: {n}")

#for i in range(15, 2, -1):
#    print(f"i: {i}")

#!SECTION

#SECTION - The arguments range accepts are similar to slicing

message = "value exalt apprise esteem"
print(f"{message[6:19:2]}")

print(list(range(6,18,2)))


#!SECTION
 