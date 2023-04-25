class State:
    def review(self, doc):
        pass

    def approve(self, doc):
        pass

    def print(self, doc):
        pass


class Document:
    def __init__(self, content, state):
        self.content = content
        self.state = state

    def review(self):
        self.state.review(self)

    def approve(self):
        self.state.approve(self)

    def print(self):
        self.state.print(self)

    def setState(self, state):
        self.state = state

    def getContent(self):
        return self.content


class DraftState(State):
    def review(self, doc):
        doc.setState(ReviewState())

    def approve(self, doc):
        print("Cannot approve document in draft state")

    def print(self, doc):
        print("Cannot print document in draft state")


class ReviewState(State):
    def review(self, doc):
        print("Cannot review document in review state")

    def approve(self, doc):
        doc.setState(ApproveState())

    def print(self, doc):
        print("Cannot print document in review state")


class ApproveState(State):
    def review(self, doc):
        print("Cannot review document in approve state")

    def approve(self, doc):
        print("Cannot approve document in approve state")

    def print(self, doc):
        print(doc.getContent())


if __name__ == "__main__":
    doc = Document("Hello world", DraftState())
    # in draft state
    doc.print()

    # move to review state
    doc.review()

    doc.print()

    # move to approve state
    doc.approve()
    doc.print()
