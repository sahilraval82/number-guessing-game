# Number Guessing Game - Python

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_runnig = True

print("Python Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num} ")

while is_runnig:
    guess = input("Enter Your Guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("that number is out of range")
            print(f"Select a number between {lowest_num} and {highest_num} ")

        elif guess > answer:
            print("Too High! Try again!")
        elif guess < answer:
             print("Too Low! Try again!")
        else:
            print(f"CORRECT! The Guess Answer {answer} ")
            print(f"Number of Guesses: {guesses}")

            is_runnig = False

    else:
        print("Invalid Guess")
        print(f"Select a number between {lowest_num} and {highest_num} ")