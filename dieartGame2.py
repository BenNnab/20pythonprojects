import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●    ● │",
        "│         │",
        "│  ●    ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘")
}

def roll_dice(num_of_dice):
    dice = [random.randint(1, 6) for _ in range(num_of_dice)]
    total = sum(dice)
    return dice, total

def print_dice(dice):
    for line in range(5):
        for die in dice:
            print(dice_art[die][line], end=" ")
        print()

def main():
    while True:
        try:
            num_of_dice = int(input("How many dice?: "))
            if num_of_dice <= 0:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid entry. Please enter a number.")
            continue

        dice, total = roll_dice(num_of_dice)
        print_dice(dice)
        print(f"Total score: {total}")

        replay = input("Do you want to roll again? (yes/no): ").strip().lower()
        if replay != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
