import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display, banking_receipt, prediction")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    # elif command == "banking_receipt":
    #     account.banking_receipt()
    elif command == "prediction":
        interest = float(input("Give the initial interest of your savings: "))
        year = int(input("Give the year the prediction is for: "))
        account_balance = account.account_prediction(interest, year)
        print(f"Your savings in {year} will be:  ${account_balance}")
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()