import datetime
import pytz


class Account:
    """Simple account class with balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transactions = [(Account._current_time(), balance)]
        print(f"Account created for {self._name}")
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transactions.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transactions.append((Account._current_time(), -amount))
        else:
            print("Insufficient balance")
        self.show_balance()

    def show_balance(self):
        print(f"Balance is {self.__balance}$")

    def show_transactions(self):
        for date, amount in self._transactions:
            if amount > 0:
                transaction_type = "deposited"
            else:
                transaction_type = "withdrawn"
                amount *= -1
            print(f"{amount:6} {transaction_type} on {date} (local time was {date.astimezone()})")


if __name__ == "__main__":
    print("+" * 110)
    tim = Account("Tim", 0)

    tim.deposit(1000)
    tim.withdraw(500)
    tim.withdraw(5000)

    tim.show_transactions()

    print("+" * 110)
    steph = Account("Steph", 800)
    steph.__balance = 200
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()
    steph.show_balance()
    print(steph.__dict__)

    steph._Account__balance = 40
    steph.show_balance()

    print("+" * 110)
