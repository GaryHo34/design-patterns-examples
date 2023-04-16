#include <iostream>
#include <string>

using namespace std;

class IOperatorStrategy
{
public:
    virtual void calculate(int a, int b) = 0;
    virtual ~IOperatorStrategy() {}
};

class AddOperator : public IOperatorStrategy
{
public:
    void calculate(int a, int b)
    {
        cout << "The result of " << a << " + " << b << " = " << a + b << endl;
    }
};

class SubOperator : public IOperatorStrategy
{
public:
    void calculate(int a, int b)
    {
        cout << "The result of " << a << " - " << b << " = " << a - b << endl;
    }
};

class MulOperator : public IOperatorStrategy
{
public:
    void calculate(int a, int b)
    {
        cout << "The result of " << a << " * " << b << " = " << a * b << endl;
    }
};

class DivOperator : public IOperatorStrategy
{
public:
    void calculate(int a, int b)
    {
        cout << "The result of " << a << " / " << b << " = " << a / b << endl;
    }
};

class Calculator
{
private:
    IOperatorStrategy *m_strategy;

public:
    Calculator(IOperatorStrategy *strategy) : m_strategy(strategy) {}
    void calculate(int a, int b)
    {
        m_strategy->calculate(a, b);
    }
    void setStrategy(IOperatorStrategy *strategy)
    {
        m_strategy = strategy;
    }
};

// as a client
int main(int argc, char *argv[])
{
    Calculator *calculator = new Calculator(new AddOperator());
    calculator->calculate(1, 2);

    calculator->setStrategy(new SubOperator());
    calculator->calculate(1, 2);

    calculator->setStrategy(new MulOperator());
    calculator->calculate(1, 2);

    calculator->setStrategy(new DivOperator());
    calculator->calculate(1, 2);
    return 0;
}