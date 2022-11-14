package Queue;

/*
 * Implement following
 * add: Add element to the end of the Queue.
 * remove: Remove element from the head of the Queue.
 * empty: Check if Stack is empty or not.
 * front: Returns head element from the Queue without removing it.
 * back: Returns end element from the Queue without removing it.
 * */

public class Queue<T> {
    private final T[] array;
    private final int capacity;
    private int front, rear, size;

    @SuppressWarnings("unchecked")
    Queue(int capacity) {
        this.capacity = capacity;
        this.array = (T[]) new Object[capacity];
        this.front = this.rear = this.size = 0;
    }

    public void enqueue(T item) {
        if (full())
            throw new StackOverflowError();
        this.array[this.rear] = item;
        this.rear = (this.rear + 1) % this.capacity;
        this.size++;
    }

    public T dequeue() {
        if (empty())
            throw new NullPointerException();
        T temp = this.array[this.front];
        this.front = (this.front + 1) % this.capacity;
        this.size--;
        return temp;
    }

    public T front() {
        return this.array[this.front];
    }

    public T back() {
        return this.rear - 1 < 0 ? this.array[this.capacity - 1] : this.array[this.rear - 1];
    }

    private boolean full() {
        return this.size == this.capacity;
    }

    private boolean empty() {
        return this.size == 0;
    }

    public static void main(String[] args) {
        Queue<Integer> intQueue = new Queue<Integer>(5);
        intQueue.enqueue(1);
        intQueue.enqueue(2);
        System.out.println(intQueue.dequeue());
        System.out.println(intQueue.dequeue());
        intQueue.enqueue(7);
        intQueue.enqueue(9);
        intQueue.enqueue(5);
        intQueue.enqueue(6);
        intQueue.enqueue(4);
        System.out.println(intQueue.front());
        System.out.println(intQueue.back());

        Queue<String> stringQueue = new Queue<String>(5);
        stringQueue.enqueue("apple");
        stringQueue.enqueue("banana");
        System.out.println(stringQueue.dequeue());
        System.out.println(stringQueue.dequeue());
        stringQueue.enqueue("orange");
        stringQueue.enqueue("Strawberry");
        stringQueue.enqueue("tomato");
        System.out.println(stringQueue.front());
        System.out.println(stringQueue.back());
    }
}
