from datetime import datetime
from banner import display_banner
# Create a bank account class for Bank clients operations

current_date =  datetime.now()
current_year = current_date.year

class BankAccount:
    # A bank account with initial balance of $0
    def __init__(self, balance = 0):
        self.balance = float(balance)

    def display_balance(self):
        """ Account balance display """
        print("Current Balance: ${:.2f}".format(self.balance))
    def deposit(self,amount):
        """ Deposit operation on the account """
        try:
            self.balance += amount
            return True
        except:
            return False
    def withdraw(self,amount):
        """ Withdrawal operation on the account """
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False
    #To be added in new version
    # def banking_receipt(self):
    #     print(f"The account number is: {self.account_id}")
    #     print(f"{self.type} account")
    #     display_banner()
    #     print(f"You account balance is: ${self.balance} ")
    # Custom function to estimate bank account balance with a certain interest in the future
    
    def account_prediction(self, interest, year):
        """ Balance prediction on the account applying interest after a certain number of years."""
        duration = year - current_year
        gain = (self.balance * interest /100) * duration
        future_balance = self.balance + gain
        return(future_balance)