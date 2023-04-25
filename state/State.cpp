#include <iostream>
#include <string>

using namespace std;
class Document;

class State
{
public:
    virtual void review(Document *) = 0;
    virtual void approve(Document *) = 0;
    virtual void print(Document *) = 0;
    virtual ~State() {}
};

class Document
{
private:
    string content;
    State *state;

public:
    Document(string content, State *state)
    {
        this->content = content;
        this->state = state;
    }
    string getContent()
    {
        return content;
    };
    void review()
    {
        state->review(this);
    }
    void approve()
    {
        state->approve(this);
    }
    void print()
    {
        state->print(this);
    }
    void setState(State *state)
    {
        this->state = state;
    }
};

class DraftState: public State
{
public:
    void review(Document *doc);
    void approve(Document *doc);
    void print(Document *doc);
};

class ReviewState: public State
{
public:
    void review(Document *doc);
    void approve(Document *doc);
    void print(Document *doc);
};

class ApprovedState: public State
{
public:
    void review(Document *doc);
    void approve(Document *doc);
    void print(Document *doc);
};

void DraftState::review(Document *doc)
{
    doc->setState(new ReviewState());
    cout << "Draft state: review" << endl;
}
void DraftState::approve(Document *doc)
{
    doc->setState(new ApprovedState());
    cout << "Draft state: approve" << endl;
}
void DraftState::print(Document *doc)
{
    cout << "Draft state: not allow to print" << endl;
}

void ReviewState::review(Document *doc)
{
    cout << "Review state: not allow to review" << endl;
}
void ReviewState::approve(Document *doc)
{
    doc->setState(new ApprovedState());
    cout << "Review state: approve" << endl;
}
void ReviewState::print(Document *doc)
{
    cout << "Review state: not allow to print" << endl;
}

void ApprovedState::review(Document *doc)
{
    cout << "Approved state: not allow to review" << endl;
}
void ApprovedState::approve(Document *doc)
{
    cout << "Approved state: not allow to approve" << endl;
}
void ApprovedState::print(Document *doc)
{
    cout << doc->getContent() << endl;
}

// as a client
int main(int argc, char *argv[])
{
    Document *doc = new Document("Hello", new DraftState());
    // When in draft state
    doc->print();

    // Move to review statte
    doc->review();
    doc->print();

    // Move to approve state
    doc->approve();
    doc->print();

    delete doc;
}