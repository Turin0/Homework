import threading
import time


class BankAcc:

    def __init__(self, lock):
        self.balance = 10000
        self.balanceLock = lock

    def deposit(self, amount):
        with self.balanceLock:
            self.balance += amount

    def withdraw(self, amount):
        with self.balanceLock:
            self.balance -= amount


def deposit_task(account, amount):
    for _ in range(10):
        account.deposit(amount)
        print(account.balance)


def withdraw_task(account, amount):
    for _ in range(10):
        account.withdraw(amount)
        print(account.balance)


lock_ = threading.Lock()
acc = BankAcc(lock=lock_)
deposit_thread = threading.Thread(target=deposit_task, args=(acc, 150))
withdraw_thread = threading.Thread(target=withdraw_task, args=(acc, 100))

deposit_thread.start()
time.sleep(0.002)
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
