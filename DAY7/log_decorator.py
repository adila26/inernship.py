from functools import wraps
from datetime import datetime
def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now()
        with open("log.txt", "a") as file:
            file.write(
                f"{timestamp} | {func.__name__} | args={args} | kwargs={kwargs}\n"
            )
        return func(*args, **kwargs)
    return wrapper
@log_call
def add(a, b):
    return a + b
@log_call
def greet(name):
    return f"Hello, {name}"
@log_call
def multiply(a, b):
    return a * b
add(10, 20)
add(5, 3)
greet("Adila")
greet("John")
multiply(2, 4)
multiply(5, 6)
multiply(7, 8)
def read_logs():
    counts = {}
    with open("log.txt", "r") as file:
        for line in file:
            parts = line.split("|")
            if len(parts) >= 2:
                func_name = parts[1].strip()
                counts[func_name] = counts.get(func_name, 0) + 1
    print("\nFunction Call Counts:")
    for func, count in counts.items():
        print(f"{func}: {count}")
read_logs()