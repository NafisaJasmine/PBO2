try:
    x = 3
    y = "Hello World"
    x + y
except TypeError:
    print("unsupported operand type(s) for +: 'int' and 'str'")