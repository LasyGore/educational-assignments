import threading

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f"Deposited {amount}, new balance is {self.balance}")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}, new balance is {self.balance}")
            else:
                print(f"Insufficient funds. Current balance: {self.balance}")

def deposit_task(account, amount):
    for _ in range(10):
        account.deposit(amount)

def withdraw_task(account, amount):
    for _ in range(10):
        account.withdraw(amount)

if __name__ == "__main__":
    account = BankAccount(1000)

    deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
    withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

    deposit_thread.start()
    withdraw_thread.start()

    deposit_thread.join()
    withdraw_thread.join()

#Пояснение:

#Я создал класс BankAccount для представления банковского счета. Он имеет атрибут balance для хранения баланса и lock
# для блокировки доступа к общему ресурсу.
#Методы deposit и withdraw используют контекстный менеджер with self.lock: для блокировки доступа
# к балансу во время модификации.
#Функции deposit_task и withdraw_task имитируют соответствующие операции, вызывая методы deposit и withdraw 10 раз.
#ТАк же учтена возможность исчерпания денег на счете. (ПРоверена - работает.)
#В if __name__ == "__main__": я создаю объект BankAccount с начальным балансом 1000, запускаю два потока
# для выполнения задач пополнения и снятия денег, а затем жду их завершения.
#Это решение гарантирует, что доступ к общему ресурсу (балансу счета) будет защищен от гонок,
# и операции пополнения и снятия будут выполняться корректно.