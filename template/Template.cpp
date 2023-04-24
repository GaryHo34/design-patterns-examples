#include <iostream>
#include <string>

using namespace std;

class WorkerTemplate
{
public:
    void execute()
    {
        startWork();
        doWork();
        endWork();
    }
    void startWork()
    {
        cout << "Start work" << endl;
    }
    void endWork()
    {
        cout << "End work" << endl;
    }

    virtual void doWork() = 0;
    virtual ~WorkerTemplate() {}
};

class HRWorker : public WorkerTemplate
{
public:
    void doWork()
    {
        cout << "HR worker do work" << endl;
    }
};

class ManagerWorker : public WorkerTemplate
{
public:
    void doWork()
    {
        cout << "Manager worker is managing task" << endl;
    }
};

class DeveloperWorker : public WorkerTemplate
{
public:
    void doWork()
    {
        cout << "Developer worker is writing code" << endl;
    }
};

// as a client
int main(int argc, char *argv[])
{
    WorkerTemplate *worker = new HRWorker();
    worker->execute();
    delete worker;

    worker = new ManagerWorker();
    worker->execute();
    delete worker;

    worker = new DeveloperWorker();
    worker->execute();
    delete worker;
    return 0;
}