#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

class BulletType
{
public:
    int speed;
    int damage;
    string name;
    BulletType(string name, int speed, int damage)
    {
        this->name = name;
        this->speed = speed;
        this->damage = damage;
    }
};

class Bullet
{
private:
    int x;
    int y;
    BulletType *type;

public:
    Bullet(int x, int y, BulletType *type)
    {
        this->x = x;
        this->y = y;
        this->type = type;
    }

    void describe()
    {
        cout << "Bullet " << this->type->name << endl;
        cout << "Speed " << this->type->speed << endl;
        cout << "Damage " << this->type->damage << endl;
        cout << "@ (" << x << ", " << y << ")" << endl;
    }
};

class BulletFactory
{
private:
    unordered_map<string, BulletType *> bulletTypes;

public:
    Bullet *getBullet(string name, int x, int y)
    {
        BulletType *type = bulletTypes[name];
        if (type == NULL)
        {
            type = new BulletType(name, 10, 10);
            bulletTypes[name] = type;
        }
        return new Bullet(x, y, type);
    }
};

int main()
{
    BulletFactory *factory = new BulletFactory();
    Bullet *bullet1 = factory->getBullet("AK47", 0, 0);
    Bullet *bullet2 = factory->getBullet("AK47", 0, 10);
    bullet1->describe();
    bullet2->describe();

    Bullet *bullet3 = factory->getBullet("M4A1", 0, 10);
    Bullet *bullet4 = factory->getBullet("M4A1", 0, 20);

    bullet3->describe();
    bullet4->describe();
}