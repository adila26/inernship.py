import random
secret_number=random.randint(1,100)
print("Guess the number between 1 and 100")
while True:
    Guess=int(input("enter your Guess:"))
    if Guess > secret_number:
        print("Too high!")
    elif Guess < secret_number:
        print("Too low!")
    else:
         print("Correct! You Guessed The Number.")
         break