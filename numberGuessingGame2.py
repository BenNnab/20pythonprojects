import random

def play_game():
    lowest_num = 1
    highest_num = 100

    answer = random.randint(lowest_num, highest_num)
    guesses = 0

    print("Python Number Guessing Game")
    print(f"Enter a number between {lowest_num} and {highest_num}")

    while True:
        try:
            guess = int(input("Enter your guess number: "))
            guesses += 1

            if guess < lowest_num or guess > highest_num:
                print(f"The number you entered is out of range. Please enter a number between {lowest_num} and {highest_num}.")
            elif guess < answer:
                print("Too low! Try again.")
            elif guess > answer:
                print("Too high! Try again.")
            else:
                print(f"CORRECT! The answer was {answer}.")
                print(f"Your total number of guesses: {guesses}")
                break
        except ValueError:
            print(f"Invalid entry. Please enter a number between {lowest_num} and {highest_num}.")

def main():
    while True:
        play_game()
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
