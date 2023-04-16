
public class Strategy {

    private interface IOperatorStrategy {
        public int calculate(int a, int b);
    }

    private class AddOperator implements IOperatorStrategy {
        @Override
        public int calculate(int a, int b) {
            System.out.println("The result of " + a + " + " + b + " =");
            return a + b;
        }
    }

    private class SubOperator implements IOperatorStrategy {
        @Override
        public int calculate(int a, int b) {
            System.out.println("The result of " + a + " - " + b + " =");
            return a - b;
        }
    }

    private class MulOperator implements IOperatorStrategy {
        @Override
        public int calculate(int a, int b) {
            System.out.println("The result of " + a + " * " + b + " =");
            return a * b;
        }
    }

    private class DivOperator implements IOperatorStrategy {
        @Override
        public int calculate(int a, int b) {
            System.out.println("The result of " + a + " / " + b + " =");
            return a / b;
        }
    }

    // Another way to implement the strategy pattern is to use enum and lambda expression.
    private class LambdaStartegy {
        // Each constants will execute the same constructor.
        public enum EnumOperatorStrategy implements IOperatorStrategy {
            ADD((int a, int b)->{
                System.out.println("The result of " + a + " + " + b + " =");
                return a + b;
            }),
            SUB((int a, int b)->{
                System.out.println("The result of " + a + " - " + b + " =");
                return a - b;
            }),
            MUL((int a, int b)->{
                System.out.println("The result of " + a + " * " + b + " =");
                return a * b;
            }),
            DIV((int a, int b)->{
                System.out.println("The result of " + a + " / " + b + " =");
                return a / b;
            });
            
            private final IOperatorStrategy operator;

            // We can define the enum's constructor here
            EnumOperatorStrategy(IOperatorStrategy operator) {
                this.operator = operator;
            }

            @Override
            public int calculate(int a, int b) {
                return operator.calculate(a, b);
            }
        }
    }

    private class Calculator {
        private IOperatorStrategy operator;

        public Calculator(IOperatorStrategy operator) {
            this.operator = operator;
        }

        public int calculate(int a, int b) {
            return operator.calculate(a, b);
        }
    }

    public void testCalculator() {
        Calculator calculator = new Calculator(LambdaStartegy.EnumOperatorStrategy.ADD);
        System.out.println(calculator.calculate(1, 2));

        calculator = new Calculator(new SubOperator());
        System.out.println(calculator.calculate(1, 2));

        calculator = new Calculator(new MulOperator());
        System.out.println(calculator.calculate(1, 2));

        calculator = new Calculator(new DivOperator());
        System.out.println(calculator.calculate(1, 2));
    }


    public static void main(String[] args) {
        Strategy strategy = new Strategy();
        strategy.testCalculator();
    }
}