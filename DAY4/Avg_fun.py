def average(*marks):
    if len(marks) == 0:
        return "No marks provided"
    return sum(marks) / len(marks)
print(average(70, 80, 90))
print(average(40, 65))
print(average())