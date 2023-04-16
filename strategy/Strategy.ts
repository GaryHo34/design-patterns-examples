
interface IOperatorStrategy {
    calculate: (a: number, b: number) => number;
}

class AddOperator implements IOperatorStrategy {
    public calculate(a: number, b: number): number {
        console.log("The result of " + a + " + " + b + " =");
        return a + b;
    }
}

class SubtractOperator implements IOperatorStrategy {
    public calculate(a: number, b: number): number {
        console.log("The result of " + a + " - " + b + " =");
        return a - b;
    }
}

class MultiplyOperator implements IOperatorStrategy {
    public calculate(a: number, b: number): number {
        console.log("The result of " + a + " * " + b + " =");
        return a * b;
    }
}

class DivideOperator implements IOperatorStrategy {
    public calculate(a: number, b: number): number {
        console.log("The result of " + a + " / " + b + " =");
        return a / b;
    }
}

class Calculator {
    private operator: IOperatorStrategy;
    constructor(operator: IOperatorStrategy) {
        this.operator = operator;
    }
    public setOperator(operator: IOperatorStrategy) {
        this.operator = operator;
    }

    public calculate(a: number, b: number): number {
        return this.operator.calculate(a, b);
    }
}

const testStrategy = () => {
    const calculator = new Calculator(new AddOperator());
    console.log(calculator.calculate(1, 2));
    calculator.setOperator(new SubtractOperator());
    console.log(calculator.calculate(1, 2));
    calculator.setOperator(new MultiplyOperator());
    console.log(calculator.calculate(1, 2));
    calculator.setOperator(new DivideOperator());
    console.log(calculator.calculate(1, 2));
}

testStrategy();