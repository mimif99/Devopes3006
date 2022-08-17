def print_hello(name):
    if name != "michael":
        print(f"hello {name}")


def greet_name(name, excluded_name="michael", greeting_word="hello"):
    if name != excluded_name:
        return f"{greeting_word} {name}"


def multiply(x, y, c):
    from utils import important_var
    result1 = x * y
    result2 = x / y
    return result1, result2


r, r2 = multiply(4, 2, 1)
print(r[0])
print(r[1])
