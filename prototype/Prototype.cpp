#include <chrono>
#include <iostream>
#include <thread>
#include <vector>

using namespace std;

class DataSet
{
private:
    int id;

public:
    vector<int> data;
    DataSet()
    {
        // wait 5 seconds
        cout << "Loading data from disk..." << endl;
        std::this_thread::sleep_for(std::chrono::milliseconds(5000));
    }

    // Copy constructor
    DataSet(const DataSet &other)
    {
        id = other.id;
        // vector defaultly use copy assignment operator
        data = other.data;
    }

    // Copy assignment operator
    DataSet &operator=(const DataSet &other)
    {
        id = other.id;
        // vector defaultly use copy assignment operator
        data = other.data;
        return *this;
    }

    DataSet clone()
    {
        DataSet clone = *this;
        return clone;
    }
};

void testPrototype()
{
    DataSet ds1;
    DataSet ds2 = ds1.clone();
    DataSet ds3 = ds1;

    ds1.data.push_back(1);
    ds2.data.push_back(2);
    ds3.data.push_back(3);

    cout << "ds1: " << ds1.data[0] << endl;
    cout << "ds2: " << ds2.data[0] << endl;
    cout << "ds3: " << ds3.data[0] << endl;
}

int main(int argc, char **argv)
{
    testPrototype();
    return 0;
}