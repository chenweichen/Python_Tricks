
class Car:
    rev = lambda self,x: print(f"x: {x}")
    crash = lambda self: print("Boom")

#my_car = Car()
#my_car.crash()
#my_car.rev(20)


print(list(filter(lambda x: x % 2 ==0, range(16))))

print([x for x in range(16) if x%2 ==0])
