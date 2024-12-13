import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def show_balance(balance):
    print(f"Your current balance is ${balance:,.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))    
    if amount < 0:
        print("That is an invalid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))
    if amount > balance:
        print("Insufficient balance")
        return 0
    elif amount < 0:
        print("Amount must be greater than $0")
        return 0
    else:
        return amount

def show_transaction_history(transaction_history):
    if not transaction_history:
        print("No transactions to show.")
    else:
        for transaction in transaction_history:
            print(transaction)

def filter_transaction_history(transaction_history, start_date, end_date):
    filtered_transactions = []
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")
    
    for transaction in transaction_history:
        timestamp_str = transaction.split(" - ")[0]
        timestamp = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        
        if start_date <= timestamp <= end_date:
            filtered_transactions.append(transaction)
    
    return filtered_transactions

def print_to_pdf(filtered_transactions):
    file_name = "transaction_history.pdf"
    pdf = canvas.Canvas(file_name, pagesize=letter)
    pdf.setTitle("Transaction History")
    
    pdf.drawString(30, 750, "Transaction History:")
    y = 730
    for transaction in filtered_transactions:
        pdf.drawString(30, y, transaction)
        y -= 20
    
    pdf.save()
    print(f"Transaction history saved to {file_name}")

def main():
    balance = 0
    transaction_history = []
    is_running = True
    while is_running:
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Show Transaction History")
        print("5. Filter Transaction History by Date")
        print("6. Exit")
        
        choice = input("Enter your choice (1 - 6):")
        
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            amount = deposit()
            if amount != 0:
                balance += amount
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                transaction_history.append(f"{timestamp} - Deposited: ${amount:,.2f}")
        elif choice == '3':
            amount = withdraw(balance)
            if amount != 0:
                balance -= amount
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                transaction_history.append(f"{timestamp} - Withdrew: ${amount:,.2f}")
        elif choice == '4':
            show_transaction_history(transaction_history)
        elif choice == '5':
            start_date = input("Enter start date (YYYY-MM-DD HH:MM:SS): ")
            end_date = input("Enter end date (YYYY-MM-DD HH:MM:SS): ")
            filtered_transactions = filter_transaction_history(transaction_history, start_date, end_date)
            show_transaction_history(filtered_transactions)
            print_to_pdf(filtered_transactions)
        elif choice == '6':
            is_running = False
        else:
            print("You have made an invalid choice")
            
        print("Thank you for Banking with us, do have a nice day!")

if __name__ == "__main__":
    main()
