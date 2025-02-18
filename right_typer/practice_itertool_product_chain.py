
#for i in range(10):
#    for j in range(3):
#        print(f"(i,j): {(i,j)}")

from itertools import product

#for i, j in product(range(10), range(3)):
#    print(f"(i,j): {(i,j)}")

#a_l = list(range(5))
#b_l = list(range(3))
#f_l = a_l + b_l 
#for ele in f_l:
#    print(f"ele: {ele}")

from itertools import chain
#for ele in chain(a_l, b_l):
#    print(f"ele: {ele}")


#for x in range(1, 10):
#    print(x)

#for x in range(1, 11):
#    print(x)

#for x in range(10, 0, -1):
#    print(f"Reverse: {x}")

for y in range(10, -1, -1):
    print(f"Reverse: {y}")

for y in range(10, -1, -2):
    print(f"Reverse: {y}")