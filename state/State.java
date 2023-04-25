public class State {
    private abstract class IState {
        public abstract void review(Document doc);

        public abstract void approve(Document doc);

        public abstract void print(Document doc);
    }

    private class Document {
        String content;
        IState state;

        public Document(String content, IState state) {
            this.content = content;
            this.state = state;
        }

        public void review() {
            state.review(this);
        }

        public void approve() {
            state.approve(this);
        }

        public void print() {
            state.print(this);
        }

        public void setState(IState state) {
            this.state = state;
        }

        public String getContent() {
            return content;
        }
    }

    private class DraftState extends IState {
        public void review(Document doc) {
            doc.setState(new ReviewState());
        }

        public void approve(Document doc) {
            System.out.println("Cannot approve document in draft state");
        }

        public void print(Document doc) {
            System.out.println("Cannot print document in draft state");
        }
    }

    private class ReviewState extends IState {
        public void review(Document doc) {
            System.out.println("Cannot review document in review state");
        }

        public void approve(Document doc) {
            doc.setState(new ApproveState());
        }

        public void print(Document doc) {
            System.out.println("Cannot print document in review state");
        }
    }

    private class ApproveState extends IState {
        public void review(Document doc) {
            System.out.println("Cannot review document in approve state");
        }

        public void approve(Document doc) {
            System.out.println("Cannot approve document in approve state");
        }

        public void print(Document doc) {
            System.out.println(doc.getContent());
        }
    }

    void testState() {
        Document doc = new Document("Hello world", new DraftState());
        // in draft state
        doc.print();

        // move to review state
        doc.review();
        doc.print();

        // move to approve state
        doc.approve();
        doc.print();
    }

    public static void main(String[] args) {
        State st = new State();
        st.testState();
    }
}