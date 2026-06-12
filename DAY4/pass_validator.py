class WeakPasswordError(Exception):
    pass
def validate_password(password):
    if len(password) < 8:
        raise WeakPasswordError("Password must be at least 8 characters long.")
    if not any(char.isdigit() for char in password):
        raise WeakPasswordError("Password must contain at least one digit.")
    if not any(char.isupper() for char in password):
        raise WeakPasswordError("Password must contain at least one uppercase letter.")
    return "Password is valid."
try:
    pwd = input("Enter password: ")
    print(validate_password(pwd))
except WeakPasswordError as e:
    print("Error:", e)
