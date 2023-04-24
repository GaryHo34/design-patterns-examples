# Template Pattern

Template pattern is a behavioral pattern that defines the skeleton of an algorithm in a method, deferring some steps to subclasses. Template method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure. 
Let's take a look at the example below. We have a class `WorkerTemplate` that defines the skeleton of an algorithm in a method `execute()`. The method `execute()` calls three methods: `startWork()`, `doWork()` and `finishWork()`. The method `doWork()` is abstract and is implemented in subclasses. The method `execute()` is final, so it can't be overridden in subclasses.


```java

public abstract class WorkerTemplate {
    public final void execute() {
        startWork();
        doWork();
        finishWork();
    }

    public void startWork() {
        System.out.println("Start working");
    }

    public abstract void doWork();

    public void finishWork() {
        System.out.println("Finish working");
    }

}
public class HRWorker extends WorkerTemplate {
    @Override
    public void doWork() {
        System.out.println("HR worker is working");
    }
}

public class DeveloperWorker extends WorkerTemplate {
    @Override
    public void doWork() {
        System.out.println("Developer worker is writing code");
    }
}

public class Main {
    public static void main(String[] args) {
        WorkerTemplate worker = new HRWorker();
        worker.execute();
        worker = new DeveloperWorker();
        worker.execute();
    }
}
```

