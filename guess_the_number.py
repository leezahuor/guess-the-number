import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    guess_limit = 3 
    while guess_limit != 0:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry guess again - too low! You have " + str(guess_limit) + " guesses left.")
        elif guess > random_number:
            print("Sorry guess again - too high! You have " + str(guess_limit) + " guesses left.")
        else:
            print (f"Your guess was correct! It was {random_number}")
            return
        guess_limit -= 1
    print(f"Out of guesses, you lose! The number was {random_number}")

guess(10) 