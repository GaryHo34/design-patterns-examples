// Since we JavaScript is a single threaded language, we can use a static variable to store the instance of the class.

class BankAccount {
    private static instance: BankAccount;
    private balance: number = 100;
    private constructor() { }

    public static getInstance(): BankAccount {
        if (!this.instance) {
            this.instance = new BankAccount();
        }
        return this.instance;
    }
    getBalance() {
        return this.balance;
    }
    withdraw() {
        this.balance -= 10;
    }
}

const account = BankAccount.getInstance();
account.withdraw();
console.log(account.getBalance());
