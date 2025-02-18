
class Adder:
    def __init__(self, n: int):
        self._n = n

    def __call__(self, x: int):
        return self._n  + x 
    
plus_2 = Adder(2)
print(f"{plus_2(3)}")


class MyAdder:
    def __init__(self, x: int):
        self._x  = x

    def __call__(self, n: int):
        return self._x + n 
    
myAdd_3 = MyAdder(3)
print(f"{myAdd_3(5)}")


class HerAdder:
    def __init__(self, n: int):
        self._n = n

    def __call__(self, x: int):
        return self._n + x 
    
herAdder_5 = HerAdder(5)
print(f"{herAdder_5(6)}")
