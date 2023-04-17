/**
 * There are many ways to implement the thread safe singleton pattern.
 * I suggest you to read the following article:
 * https://www.modernescpp.com/index.php/thread-safe-initialization-of-a-singleton
 *
 * We will implement it using aquire/release semantics.
 */

#include <iostream>
#include <atomic>
#include <iostream>
#include <future>
#include <mutex>
#include <thread>
#include <string>

using namespace std;

class BankAccount
{
private:
    // The std::atomic class template is a template that allows to perform atomic operations on integral types.
    static std::atomic<BankAccount *> instance;
    // This is the mutex that will be used to lock the critical section.
    static std::mutex mtx;
    int balance;

    // To make a class singleton, we need to make the constructor private.
    BankAccount()
    {
        balance = 100;
    };

    ~BankAccount() = default;
    // we will ban the copy constructor and the assignment operator.
    BankAccount(const BankAccount &) = delete;
    BankAccount &operator=(const BankAccount &) = delete;

public:
    static BankAccount *getInstance()
    {
        BankAccount *ac = instance.load(std::memory_order::memory_order_acquire);
        if (!ac)
        {
            std::lock_guard<std::mutex> lock(mtx);
            ac = instance.load(std::memory_order::memory_order_relaxed);
            if (!ac)
            {
                ac = new BankAccount();
                instance.store(ac, std::memory_order::memory_order_release);
            }
        }
        return ac;
    }

    void withdraw()
    {
        balance -= 10;
    }

    double getBalance()
    {
        return balance;
    }
};

std::atomic<BankAccount *> BankAccount::instance;
std::mutex BankAccount::mtx;

void test_run()
{
    auto ac = BankAccount::getInstance();
    ac->withdraw();
    cout << "BankAccount: " << ac << endl;
    cout << "Balance: " << ac->getBalance() << endl;
}

int main(int argc, char *argv[])
{
    std::async(std::launch::async, test_run);
    std::async(std::launch::async, test_run);
    std::async(std::launch::async, test_run);
    std::async(std::launch::async, test_run);
    return 0;
}