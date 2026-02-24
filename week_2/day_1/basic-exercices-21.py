class Dog:
    def __init__(self, name, color, breed, age, is_trained): #the constructor function 
        self.name = name
        self.color = color
        self.breed = breed
        self.age = age
        self.is_trained = is_trained
    def run(self):
        if self.age > 5:
            print(f"{self.name} prefers to walk")
        else:
            print(f"{self.name} is running")

dog2 = Dog("Jazz", "white", "swiss white shepherd", 1, False)
print(dog2.breed)

dog2.run()

import datetime

class BankAccount:
    def __init__(self, holder, number, balance = 50.00):
        self.holder = holder
        self.number = number
        self.balance = balance
        self.transactions = [] #internal attribute

    def view_balance(self):
        self.transactions.append(f" {datetime.datetime.now()} --- view_balance")
        report = f"""account holder: {self.holder}
        account number: {self.number}
        balance: {self.balance}"""
        print(report)

    def deposit(self, amount):
        self.transactions.append(f" {datetime.datetime.now()} --- deposit {amount}")
        if amount <= 0:
            print("invalid amount")
        else:
            self.balance += amount
        self.view_balance()
        return self.balance
    
    def withdraw(self, amount):
        self.transactions.append(f" {datetime.datetime.now()} --- withdraw {amount}")
        if amount <= 0:
            print("invalid amount")
        elif self.balance < amount:
            print("You dont have enough money")
        else:
            self.balance -= amount
        self.view_balance()
        return self.balance
    
    def view_transactions(self):
        for transaction in self.transactions:
            print(transaction)


acc1 = BankAccount("John Doe", "987654")
acc1.view_balance()
acc1.deposit(500)
acc1.deposit(-50)
acc1.withdraw(700)
acc1.withdraw(200)
acc1.view_transactions()

