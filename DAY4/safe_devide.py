def safe_divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
try:
    print(safe_divide(150, 2))
    print(safe_divide(10, 0))
except ZeroDivisionError as e:
    print(e)