class Account:
    def __init__(self,balance=0):
        self.balance=balance 
    def deposit(self,amount):
        self.balance+=amount
        print("Deposited amount: ",amount)
    def withdraw(self,amount):
        if amount>self.balance:
            print("No sufficient balance")
        else:
            self.balance-=amount 
            print("Amount with drawn: ",amount)
    def display(self):
        print(f"Balance: {self.balance}")
b1=Account()
b1.deposit(5000)
b1.withdraw(500)
b1.display()
            