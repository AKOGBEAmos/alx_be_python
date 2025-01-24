from datetime import datetime
from banner import display_banner
# Create a bank account class for Bank clients operations

current_date =  datetime.now()
current_year = current_date.year

class BankAccount:
    def __init__(self, account_id, balance = 0, account_type):
        self.account_id = account_id
        self.balance = balance
        self.type = account_type

    def display_balance(self):
        print(f"Current Balance: ${self.balance}")
    def deposit(self,amount):
        try:
            self.balance += amount
            return True
        except:
            return False
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def banking_receipt(self):
        print(f"The account number is: {self.account_id}")
        print(f"{self.type} account")
        display_banner()
        print(f"You account balance is: ${self.balance} ")
    # Custom function to estimate bank account balance with a certain interest in the future
    
    def account_prediction(self, interest, year):
        duration = year - current_year
        gain = (self.balance * interest /100) * duration
        future_balance = self.balance + gain
        return(future_balance)