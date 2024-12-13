import random

# Expanded word list with different difficulties
words = {
    'easy': ["apple", "orange", "banana"],
    'medium': ["coconut", "pineapple", "strawberry"],
    'hard': ["blackberry", "raspberry", "blueberry"]
}

hangman_art = {
    0: ("   ", "   ", "   "),
    1: (" o ", "   ", "   "),
    2: (" o ", " | ", "   "),
    3: (" o ", "/| ", "   "),
    4: (" o ", "/|\\", "   "),
    5: (" o ", "/|\\", "/  "),
    6: (" o ", "/|\\", "/ \\")
}

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print("Current hint: " + " ".join(hint))

def display_guessed_letters(guessed_letters):
    print("Guessed letters: " + " ".join(sorted(guessed_letters)))

def display_answer(answer):
    print("The word was: " + answer)

def get_difficulty():
    while True:
        level = input("Choose difficulty (easy, medium, hard): ").lower()
        if level in words:
            return level
        print("Invalid choice. Please choose again.")

def main():
    difficulty = get_difficulty()
    word = random.choice(words[difficulty])
    hint = ["_" for _ in word]
    wrong_guesses = 0
    guessed_letters = []

    print("\nWelcome to Hangman!")
    while wrong_guesses < len(hangman_art) - 1 and "_" in hint:
        display_man(wrong_guesses)
        display_hint(hint)
        display_guessed_letters(guessed_letters)
        
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
        
    display_man(wrong_guesses)
    if "_" not in hint:
        print("Congratulations, you won!")
    else:
        print("You lost. Better luck next time!")
    display_answer(word)

if __name__ == "__main__":
    main()
