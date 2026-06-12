class InvalidMarkError(Exception):
    pass
def calculate_grade(name, *marks):
    if len(marks) == 0:
        raise InvalidMarkError("No marks provided")

    for mark in marks:
        if mark < 0 or mark > 100:
            raise InvalidMarkError(f"Invalid mark: {mark}")

    average = sum(marks) / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "F"

    return average, grade
def generate_report(students):
    print("-" * 40)
    print(f"{'Name':<10}{'Average':<10}{'Grade':<10}")
    print("-" * 40)

    for student in students:
        name = student[0]
        marks = student[1:]

        try:
            avg, grade = calculate_grade(name, *marks)
            print(f"{name:<10}{avg:<10.2f}{grade:<10}")

        except InvalidMarkError as e:
            print(f"{name:<10}ERROR: {e}")

    print("-" * 40)
students = [
    ("Adila", 95, 90, 92),      
   ("Shahana", 80, 70, 75),    
    ("Rana", 150, 85, 90),     
    ("Aisha",),                
    ("Fidha", 60, -5, 75)        
]
generate_report(students)