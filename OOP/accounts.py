import datetime
import pytz


class Account:
    """Simple account class with balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = []
        print(f"Account created for {self.name}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transactions.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append((Account._current_time(), -amount))
        else:
            print("Insufficient balance")
        self.show_balance()

    def show_balance(self):
        print(f"Balance is {self.balance}$")

    def show_transactions(self):
        for date, amount in self.transactions:
            if amount > 0:
                transaction_type = "deposited"
            else:
                transaction_type = "withdrawn"
                amount *= -1
            print(f"{amount:6} {transaction_type} on {date} (local time was {date.astimezone()})")


if __name__ == "__main__":
    tim = Account("Tim", 0)

    tim.deposit(1000)
    tim.withdraw(500)
    tim.withdraw(5000)

    tim.show_transactions()
