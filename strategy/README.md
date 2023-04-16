# Strategy Pattern

The strategy pattern is a behavioral design pattern that allows you to define a family of algorithms, encapsulate each one and make them interchangeable. The strategy pattern lets the algorithm vary independently from the clients that use it.

What does it mean to encapsulate an algorithm? It means that we can define a series classes called strategies, each of which implements a specific algorithm. We define a context class which has a strategy field. The context class uses the strategy field to perform its work. The context class can change the strategy field at runtime to change the algorithm it uses.

The best part for client to use the strategy pattern is that it doesn't need to know the details of the algorithm. It only needs to know the context class and the strategy interface. The context class will handle the details of the algorithm.

## Example code

Let's take a look at the basic implementation of the strategy pattern. If we have a calculator, we can define a strategy interface for each operation. The context class will use the strategy field to perform its work.

```java

// THe startegy is about the behabior of the specific operator in the calculator
public interface IOperatorStrategy {
    int calculate(int a, int b);
}

// The context class is the calculator
public class Calculator {
    private IOperatorStrategy strategy;

    public Calculator(IOperatorStrategy strategy) {
        this.strategy = strategy;
    }

    public void setStrategy(IOperatorStrategy strategy) {
        this.strategy = strategy;
    }

    public int calculate(int a, int b) {
        return strategy.calculate(a, b);
    }
}

// Let's define some strategies
public class AddStrategy implements IOperatorStrategy {
    @Override
    public int calculate(int a, int b) {
        return a + b;
    }
}

public class SubtractStrategy implements IOperatorStrategy {
    @Override
    public int calculate(int a, int b) {
        return a - b;
    }
}

// We can define a super complex calculation strategy
public class ComplexCalculationStrategy implements IOperatorStrategy {
    @Override
    public int calculate(int a, int b) {
        return a * b + a / b;
    }
}

// Now we can use the calculator
// In the client's view, we only need to know the context class and the strategy interface
public class Client {
    public static void main(String[] args) {
        Calculator calculator = new Calculator(new AddStrategy());
        System.out.println(calculator.calculate(1, 2)); // 3

        calculator.setStrategy(new SubtractStrategy());
        System.out.println(calculator.calculate(1, 2)); // -1

        calculator.setStrategy(new ComplexCalculationStrategy());
        System.out.println(calculator.calculate(1, 2)); // 3
    }
}

```