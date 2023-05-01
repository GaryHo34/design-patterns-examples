#include <iostream>
#include <string>

using namespace std;

class Shape
{
public:
    virtual void draw() = 0;
};

class RedCircle : public Shape
{
private:
    int x, y;
    string color;

public:
    RedCircle(int x, int y)
    {
        this->x = x;
        this->y = y;
        this->color = "red";
    }

    void draw()
    {
        cout << "Drawing a " << color << " circle at (" << x << ", " << y << ")" << endl;
    }
};

class BlueSquare : public Shape
{
private:
    int x, y;
    string color;

public:
    BlueSquare(int x, int y)
    {
        this->x = x;
        this->y = y;
        this->color = "blue";
    }

    void draw()
    {
        cout << "Drawing a " << color << " circle at (" << x << ", " << y << ")" << endl;
    }
};

class Drawer
{
private:
    Shape *shape;

public:
    Drawer(Shape *shape)
    {
        this->shape = shape;
    }

    void draw()
    {
        shape->draw();
    }
};

int main()
{
    Drawer *drawer = new Drawer(new RedCircle(10, 10));
    drawer->draw();
    drawer = new Drawer(new BlueSquare(20, 20));
    drawer->draw();
    return 0;
}
