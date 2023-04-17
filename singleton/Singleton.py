import threading


class BankAccount():
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        self.balance = 100

    def __new__(self):
        if not self._instance:
            with self._lock:
                if not self._instance:
                    self._instance = super().__new__(self)
        return self._instance
    
    def getBalance(self)->int:
        return self.balance

    def withdraw(self):
        self.balance -= 10

def thread_test_run():
    ac = BankAccount()
    print(ac)
    print(ac.getBalance())
    ac.withdraw()
    print(ac.getBalance())

if __name__ == '__main__':
    t1 = threading.Thread(target=thread_test_run)
    t2 = threading.Thread(target=thread_test_run)
    t1.start()
    t2.start()
