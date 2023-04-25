# State Pattern

State Pattern is a behavioral design pattern that allows an object to alter its behavior when its internal state changes. 

It is very common to use the concept of finite state machines in the daily job. For example, a document could have three states `Draft`, `Reviewing`and `Approved`. If our system is not allowed users to edit the document when it is in `Approved` state, or to print the document when it is in `Draft` state.

Let's see an example if we implement finite state machines without using State Pattern.

```java

public enum State{
    Draft,
    Reviewing,
    Approved
}

public class Document {
    String content;
    State state;

    public Document(String content) {
        this.content = content;
        this.state = State.Draft;
    }

    public void review() {
        if (this.state == State.Draft) {
            this.state = State.Reviewing;
        } else {
            throw new IllegalStateException("Document can not be reviewed in current state");
        }
    }

    public void approve() {
        if (this.state == State.Reviewing) {
            this.state = State.Approved;
        } else {
            throw new IllegalStateException("Document can not be approved in current state");
        }
    }

    public void print() {
        if (this.state == State.Approved) {
            System.out.println(this.content);
        } else {
            throw new IllegalStateException("Document can not be printed in current state");
        }
    }
}

```

Now, if we want to add some tricky features, for example, we want to add a new state `Rejected` and we want to allow users to print the document when it is in `Rejected` state. We need to modify the `Document` class and add a new method `reject()`.

```java

public enum State{
    Draft,
    Reviewing,
    Approved,
    Rejected
}

public class Document {
    // ...
    public void reject() {
        if (this.state == State.Reviewing) {
            this.state = State.Rejected;
        } else {
            throw new IllegalStateException("Document can not be rejected in current state");
        }
    }
    public void print() {
        if (this.state == State.Approved || this.state == State.Rejected) {
            System.out.println(this.content);
        } else {
            throw new IllegalStateException("Document can not be printed in current state");
        }
    }
}
```

According to the open-closed principle, we should not modify the existing code. But we have to modify the `Document` class to add the new state and the new method. If we have more states and more methods, the `Document` class will become a monster. Plus, we can find a tight coupling between the `Document` class and the `State` enum. If we want to add a new state, we have to modify the `Document` class. If we want to add a new method, we have to modify the `Document` class. If we want to add a new state and a new method, we have to modify the `Document` class. It is a nightmare.

The State Pattern can solve this problem. Let's see how to implement the State Pattern. Its core concept is to extract the state and its behavior into a separate class. 

```java

public interface State {
    void review(Document document);
    void approve(Document document);
    void reject(Document document);
    void print(Document document);
}

public class DraftState implements State {
    @Override
    public void review(Document document) {
        document.setState(new ReviewingState());
    }

    @Override
    public void approve(Document document) {
        throw new IllegalStateException("Document can not be approved in current state");
    }

    @Override
    public void reject(Document document) {
        throw new IllegalStateException("Document can not be rejected in current state");
    }

    @Override
    public void print(Document document) {
        throw new IllegalStateException("Document can not be printed in current state");
    }
}


public class Document {
    String content;
    State state;

    public Document(String content) {
        this.content = content;
        this.state = new DraftState();
    }

    public void review() {
        this.state.review(this);
    }

    public void approve() {
        this.state.approve(this);
    }

    public void reject() {
        this.state.reject(this);
    }

    public void print() {
        this.state.print(this);
    }

    public void setState(State state) {
        this.state = state;
    }
}

```

Now, the client can easily operate the `Document` class, and developer can easily add new states and new methods without modifying the `Document` class. 

```java

public class Main {
    public static void main(String[] args) {
        Document document = new Document("Hello World");
        document.review();
        document.approve();
        document.print();
    }
}

```