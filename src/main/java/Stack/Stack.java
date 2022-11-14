package Stack;

/*
 * Implement following
 * push: Push element to the top of the Stack.This operation will increase size of stack by 1.
 * pop: Remove element from the top of the Stack and returns the deleleted Object.This operation will decrease size of stack by 1.
 * empty: Check if Stack is empty or not.
 * peek: Returns top element from the stack without removing it.
 * */

import java.util.EmptyStackException;

public class Stack<T> {
    private final T[] array;
    private final int capacity;
    private int top;

    @SuppressWarnings("unchecked")
    Stack(int capacity) {
        this.array = (T[]) new Object[capacity];
        this.capacity = capacity;
        this.top = 0;
    }

    public T peek() {
        return array[top - 1];
    }

    public void push(T data) {
        if (top == capacity) {
            throw new StackOverflowError("Stack is full");
        }
        array[top] = data;
        top++;
    }

    public T pop() {
        if (empty()) {
            throw new EmptyStackException();
        }
        T data = array[top - 1];
        top--;
        return data;
    }

    public boolean empty() {
        return (top == 0);
    }

    public static void main(String[] args) {
        Stack<Integer> intStack = new Stack<Integer>(5);
        intStack.push(1);
        intStack.push(2);
        System.out.println(intStack.pop());
        System.out.println(intStack.pop());
        intStack.push(3);
        intStack.push(4);
        intStack.push(5);
        System.out.println(intStack.peek());
        System.out.println(intStack.pop());

        Stack<String> stringStack = new Stack<String>(5);
        stringStack.push("apple");
        stringStack.push("banana");
        System.out.println(stringStack.pop());
        System.out.println(stringStack.pop());
        stringStack.push("orange");
        stringStack.push("Strawberry");
        stringStack.push("tomato");
        System.out.println(stringStack.peek());
        System.out.println(stringStack.pop());
    }
}
