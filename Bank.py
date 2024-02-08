
class BankAccount:
    def __init__(self, id, name, balance):
        if balance < 5:
            raise ValueError("Initial value does not less than 5 $.")
        self.__id = id
        self.__name = name
        self.__balance = balance

    def info(self):
        return self.__id, self.__name, self.__balance

    def deposit(self, amount):
        if self.__balance + amount <= 1_000_000:
            self.__balance += amount
            return "\033[1;32m" + "OK" + "\033[0m"
        else:
            return "\033[1;31m" + "Fail" + "\033[0m"

    def withdraw(self, amount):
        if self.__balance - amount >= 5:
            self.__balance -= amount
            return "\033[1;32m" + "OK" + "\033[0m"
        else: return "\033[1;31m" + "Fail" + "\033[0m"

    def __str__(self):
        return "{:<5} {:<10} {:>20}".format(self.__id, self.__name, "\033[1;32m" + str(self.__balance) + "\033[0m")



def test(account):
    print("Before Test")
    print(account)
    print("-" * 20)

    print("Test for deposit")
    print("After testing with deposit 100$.")
    a = account.deposit(100)
    print("deposit state =", a)
    print(account)
    print("-" * 20)

    print("After testing with deposit 1_000_000$.")
    a = account.deposit(1_000_000)
    print("deposit state =", a)
    print(account)
    print("-" * 20)

    print("Test for withdraw")
    print("After testing with  100$.")
    a = account.withdraw(100)
    print("withdraw state =", a)
    print(account)
    print("-" * 20)

    print("After testing with 1_000_000$.")
    a = account.withdraw(1_000_000)
    print("withdraw state =", a)
    print(account)
    print("-" * 20)
    print("-" * 20)






