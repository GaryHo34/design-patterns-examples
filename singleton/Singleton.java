public class Singleton {
    private static class Bankaccount {
        private static volatile Bankaccount instance = null;
        private int balance;

        private Bankaccount() {
            balance = 100;
        }

        public static Bankaccount getInstance() {
            if(instance == null) {
                synchronized(Bankaccount.class) {
                    if(instance == null) {
                        instance = new Bankaccount();
                    }
                }
            }
            return instance;
        }

        public int getBalance() {
            return balance;
        }

        public void withdraw() {
            balance -= 10;
        }
    }

    private class Test implements Runnable {
        private Thread t;
        private String threadName;
        
        Test( String name) {
            threadName = name;
            System.out.println("Creating " +  threadName );
        }
        
        public void run() {
            Bankaccount ac =  Bankaccount.getInstance();
            System.out.println("The bank account is: " + System.identityHashCode(ac));
            System.out.println("The balance is: " + ac.getBalance());
            ac.withdraw();
            System.out.println("The balance is: " + ac.getBalance());
        }
        
        public void start () {
            System.out.println("Starting " +  threadName );
            if (t == null) {
                t = new Thread (this, threadName);
                t.start ();
            }
        }
    }

    public void test() {
        Test R1 = new Test( "Thread-1");
        R1.start();
        
        Test R2 = new Test( "Thread-2");
        R2.start();
    }

    public static void main(String[] args) {
        Singleton s = new Singleton();
        s.test();
    }
}
