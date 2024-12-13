# Python Number Guessing Game

import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num, highest_num)
guesses = 0

is_running = True

print("python Number Guessing Game")
print(f" Enter a number between {lowest_num} and {highest_num}")

while is_running:
     guess = input("Enter your guess number: ")
     if guess.isdigit():
         guess = int(guess)
         guesses  += 1
         
         if guess < lowest_num or guess> highest_num:
             print("The number you entered is out of range")
             print(f"Please enter a number between {lowest_num} and {highest_num}")
         elif guess < answer:
             print("Too low! Try again")
         elif guess > answer:
             print("Too high! Try again")
         else:
             print(f"CORRECT! The answer was {answer}")
             print(f"Your total number of guesses: {guesses}")
             is_running = False
     else:
         print("Invalid entry")
         print(f"Please enter a number between {lowest_num} and {highest_num}")
         