abstract class State {
    abstract review(doc: MyDocument): void;
    abstract approve(doc: MyDocument): void;
    abstract print(doc: MyDocument): void;
}

class MyDocument {
    content: string;
    state: State;

    constructor(content: string, state: State) {
        this.content = content;
        this.state = state;
    }

    review() {
        this.state.review(this);
    }

    approve() {
        this.state.approve(this);
    }

    print() {
        this.state.print(this);
    }

    setState(state: State) {
        this.state = state;
    }

    getContent(): string {
        return this.content;
    }
}

class DraftState extends State {
    review(doc: MyDocument) {
        doc.setState(new ReviewState());
    }

    approve(doc: MyDocument) {
        console.log("Cannot approve in : Documentdraft state");
    }

    print(doc: MyDocument) {
        console.log("Cannot print in : Documentdraft state");
    }
}

class ReviewState extends State {
    review(doc: MyDocument) {
        console.log("Cannot review in : Documentreview state");
    }

    approve(doc: MyDocument) {
        doc.setState(new ApproveState());
    }

    print(doc: MyDocument) {
        console.log("Cannot print in : Documentreview state");
    }
}

class ApproveState extends State {
    review(doc: MyDocument) {
        console.log("Cannot review in : Documentapprove state");
    }

    approve(doc: MyDocument) {
        console.log("Cannot approve in : Documentapprove state");
    }

    print(doc: MyDocument) {
        console.log(doc.getContent());
    }
}

const testState = () => {
    const doc: MyDocument = new MyDocument("Hello world", new DraftState());
    // in draft state
    doc.print();

    // move to review state
    doc.review();
    doc.print();

    // move to approve state
    doc.approve();
    doc.print();
}

testState();