numbers = [10, 45, 25, 89, 43]
largest = numbers[0]
second_largest = numbers[0]
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print("Second Largest:", second_largest)