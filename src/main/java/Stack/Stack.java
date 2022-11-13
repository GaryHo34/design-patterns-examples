package Stack;

/*
 * Implement following
 * push: Push element to the top of the Stack.This operation will increase size of stack by 1.
 * pop: Remove element from the top of the Stack and returns the deleleted Object.This operation will decrease size of stack by 1.
 * isEmpty: Check if Stack is empty or not.
 * isFull: Check if Stack is full or not.
 * peek: Returns top element from the stack without removing it.
 * */

import java.util.ArrayList;
import java.util.EmptyStackException;

public class Stack<T> {
    private final T[] stackArray;
    private final int size;
    private int top;

    Stack(int size) {
        this.stackArray = (T[]) new Object[size];
        this.size = size;
        this.top = 0;
    }

    public T peek() {
        return stackArray[top - 1];
    }

    public void push(T data) {
        if (top == size) {
            throw new StackOverflowError("Stack is full");
        }
        stackArray[top] = data;
        top++;
    }

    public T pop() {
        if (isEmpty()) {
            throw new EmptyStackException();
        }
        T data = stackArray[top - 1];
        top--;
        return data;
    }

    public boolean isEmpty() {
        return (top == 0);
    }

    public static void main(String[] args) {
        Stack<Integer> arr = new Stack<Integer>(5);
        arr.push(1);
        arr.push(2);
        arr.push(3);
        arr.push(4);
        arr.push(5);

        System.out.println(arr.peek());
        System.out.println(arr.pop());
        arr.push(6);
        System.out.println(arr.peek());
        System.out.println(arr.pop());
        System.out.println(arr.pop());
        System.out.println(arr.pop());
    }
}
