import random

def spin_row():
    symbols = ['🍒', '🍋', '🍉', '🍇', '⭐']  # Add actual symbols to the slots
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("'''''''''''''''''''")
    print(" | ".join(row))
    print("'''''''''''''''''''")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 5
        elif row[0] == '🍋':
            return bet * 10
        elif row[0] == '🍉':
            return bet * 15
        elif row[0] == '🍇':
            return bet * 20
        elif row[0] == '⭐':
            return bet * 30
    return 0

def main():
    balance = 100

    print("*****************************")
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🍋 🍉 🍇 ⭐")
    print("*****************************")

    while balance > 0:
        print(f"Current balance: ${balance}")
        
        bet = input("Please place your bet amount: ")
        
        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)
        
        if bet > balance:
            print("Insufficient Balance")
            continue
        if bet <= 0:
            print("Your Bet amount must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}!")
        else:
            print("Sorry you lost this round.")
        
        balance += payout

        play_again = input("Would you like to play again? (Y/N): ").upper()
        if play_again != 'Y':
            break
    
    print("***********************************************")
    print(f"Game over! Your final balance is ${balance}")
    print("Thank you for playing Python Slots!")
    print("***********************************************")

if __name__ == '__main__':
    main()
