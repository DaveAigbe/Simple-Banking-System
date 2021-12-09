class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("User Details")
        print("____________\n")
        print(f"Name: {self.name.title()}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")


class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposits(self, amount):
        self.balance += amount
        print(f"Deposit Successful | Account balance has been updated: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient Funds | Balance Available: ${self.balance}")
        else:
            self.balance -= amount
            print(f"Withdraw Successful | Account balance has been updated: ${self.balance}")

    def view_balance(self):
        self.show_details()
        print(f"| Balance Available: ${self.balance}")


