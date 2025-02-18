def get_speak_func(text: str, volume: float):
    def whisper():
        return text.lower() + "..."
    def yell():
        return text.upper() + "!"
    if volume > 0.5:
        return yell
    else:
        return whisper

print(get_speak_func("how are you", 0.9)())


def make_adder(n: int | float):
    def add(x: int | float):
        return x + n
    return add

plus_3 = make_adder(3)
print(f"{plus_3(5)}")

plus_5 = make_adder(5)
print(f"{plus_5(4)}")
