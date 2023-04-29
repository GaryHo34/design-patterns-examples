#include <iostream>
#include <string>

using namespace std;

// a demo of proxy pattern
// the proxy class is used to control the access to the real object

class Image
{
public:
    virtual void request() = 0;
};

class RealImage : public Image
{
private:
    string fileName;

public:
    RealImage(string fileName)
    {
        this->fileName = fileName;
        cout << "Loading " << fileName << endl;
    }

    void request()
    {
        cout << "Displaying " << fileName << endl;
    }
};

class ProxyImage : public Image
{
private:
    RealImage *realImage;
    string fileName;

public:
    ProxyImage(string fileName)
    {
        this->fileName = fileName;
    }

    void request()
    {
        if (realImage == NULL)
        {
            realImage = new RealImage(fileName);
        }
        realImage->request();
    }
};

int main()
{
    Image *image = new ProxyImage("test_10mb.jpg");

    // image will be loaded from disk
    image->request();
    cout << endl;

    // image has been cached, no need to load from disk
    image->request();
    cout << endl;

    return 0;
}
