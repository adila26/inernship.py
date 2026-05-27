numbers = []
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)
largest = max(numbers)
smallest = min(numbers)
total = sum(numbers)
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Numbers:", numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)
print("Sum of numbers:", total)
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)