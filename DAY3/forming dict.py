students = {
    "Adila": 85,
    "shaaah": 45,
    "afna": 72,
    "Janvi": 67,
    "afeeela": 92
}

passed = {name: mark for name, mark in students.items() if mark >= 50}

print(passed)