# Singleton Pattern

Singleton pattern is a common creational pattern. It is used to ensure that only one instance of a class is created. It is used to provide a global point of access to the object.

For example, let's say there is a bank account instance, and our program will have multiple threads accessing the bank account. If a thread create an instance and withdraw money from the account, another thread may create another instance and withdraw money from the account. This will cause the balance of the account to be incorrect. To avoid this, we can use singleton pattern to ensure that only one instance of the bank account is created.

The simplest way to have a Singleton class is to make have an static instance variable and a static method to return the instance. The constructor of the class is private so that no other class can create an instance of the class.

```java
public class BankAccount {
    private static BankAccount instance = new BankAccount();

    private BankAccount() {
    }

    public static BankAccount getInstance() {
        return instance;
    }
}
```

However, the cost for creating the instance is paid even if the instance is not used. To avoid this, we can use lazy initialization. The instance is created only when it is needed.

```java
public class BankAccount {
    private static BankAccount instance;

    private BankAccount() {
    }

    public static BankAccount getInstance() {
        if (instance == null) {
            instance = new BankAccount();
        }
        return instance;
    }
}
```

In the second example above, the instance is created when the first thread calls the `getInstance()` method. 

But the example above is not thread safe. If the first thread is creating the instance and the second thread has checked the instance is null and is about to create the instance, the second thread will create another instance. This will cause the balance of the account to be incorrect. We can design a small test to verify this.

```java
public class Singleton {
    private static Singleton instance = null;

    public static Singleton getInstance() {
        if(instance == null) {
            try {
                Thread.sleep(200);
                instance = new Singleton();
            } catch (Exception e) {
                return null;
            }
        }
        return instance;
    }
}


public class Test implements Runnable {
     private Thread t;
     private String threadName;
     
     Test( String name) {
        threadName = name;
        System.out.println("Creating " +  threadName );
     }
     
     public void run() {
        Singleton s =  Singleton.getInstance();
        System.out.println("The id of instance is: "System.identityHashCode(s));
     }
     
     public void start () {
        System.out.println("Starting " +  threadName );
        if (t == null) {
           t = new Thread (this, threadName);
           t.start ();
        }
     }
    public static void main(String[] args) {
        Test R1 = new Test( "Thread-1");
        R1.start();
        
        Test R2 = new Test( "Thread-2");
        R2.start();
    }
}

```

The output of the test is

```
Creating Thread-1
Starting Thread-1
Creating Thread-2
Starting Thread-2
The id of instance is: 1730871013
The id of instance is: 964752528
```

The two threads have created two instances of the singleton class. This is because the first thread has not finished creating the instance when the second thread has checked the instance is null and is about to create the instance.

To resolve this issue, we can use synchronized keyword to make the `getInstance()` method synchronized. This will ensure that only one thread can execute the method at a time.

```java
public class BankAccount {
    private static BankAccount instance;

    private BankAccount() {
    }

    public static synchronized BankAccount getInstance() {
        if (instance == null) {
            instance = new BankAccount();
        }
        return instance;
    }
}
```

However, the synchronized keyword is expensive. It will cause the performance of the program to be slow. To avoid this, we can use double-checked locking(DCL). The instance is created only when it is needed and the synchronized keyword is used only when the instance is null.

```java
public class BankAccount {
    private static BankAccount instance;

    private BankAccount() {
    }

    public static BankAccount getInstance() {
        if (instance == null) {
            synchronized (BankAccount.class) {
                if (instance == null) {
                    instance = new BankAccount();
                }
            }
        }
        return instance;
    }
}
```

The double-checked locking is not guaranteed to work in all JVMs. The JVM may reorder the instructions in the `getInstance()` method. The instance may be created before the instance variable is set to the instance. To avoid this, we can use volatile keyword to make the instance variable volatile.

```java
public class BankAccount {
    private static volatile BankAccount instance;

    private BankAccount() {
    }

    public static BankAccount getInstance() {
        if (instance == null) {
            synchronized (BankAccount.class) {
                if (instance == null) {
                    instance = new BankAccount();
                }
            }
        }
        return instance;
    }
}
```