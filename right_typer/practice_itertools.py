
#NOTE - [Module itertools overview](https://mathspp.com/blog/module-itertools-overview)

#SECTION - product flattens nested loops

#for x in range(5):
#    for y in range(3):
#        print(f"{(x, y)}")

#from itertools import product
#for x, y in product(range(5), range(3)):
#    print(f"{(x, y)}")

#!SECTION


#SECTION - chain creates a single iterable out of many

#first_list = ['a', 'b', 'c']
#second_list = [4,5,6]
#full_list = first_list + second_list # third_list
#for element in full_list:
#    print(f"{element}")

#from itertools import chain
#for ele in chain(first_list, second_list):
#    print(f"{ele}")

#first_gen = (x **2 for x in range(3))
#second_gen = (x **3 for x in range(3))
#for value in chain(first_gen, second_gen):
#    print(f"{value}\n")

#nested = [[1,2,3], [4], [], [5,6]]
#flat = list(chain.from_iterable(nested))
#print(flat)

#for value in chain.from_iterable(nested):
#    print(f"{value}")

#!SECTION


#SECTION - pairwise produces overlapping pairs of consecutive elements

names = ["Harry", "Anne", "George"]
#print(names[:-1])
#print(names[1:])

# slicing can be expensive if you are dealing iwth a large iterable; and
# not all iterables support slicing


for left, right in zip(names[:-1], names[1:]):
    print(f"{left} says hi to {right}")


from itertools import pairwise

names = ["Harry", "James", "Bob"]

for left, right in pairwise(names):
    print(f"{left} says hi to {right}")
    


#!SECTION