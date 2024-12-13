import random

def play_round():
    options = ("rock", "paper", "scissor")
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissor): ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a draw!")
        return 0
    elif (player == "rock" and computer == "scissor") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissor" and computer == "paper"):
        print("You win!")
        return 1
    else:
        print("You lose!")
        return -1

def main():
    player_score = 0
    computer_score = 0

    while True:
        result = play_round()
        if result == 1:
            player_score += 1
        elif result == -1:
            computer_score += 1

        print(f"Scores -> Player: {player_score}, Computer: {computer_score}")

        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
