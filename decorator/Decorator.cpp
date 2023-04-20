#include <iostream>
#include <string>

using namespace std;

// abstract class weapon interface
class IWeapon
{
public:
    virtual void describe() = 0;
    virtual int getAttack() = 0;
};

class Sword : public IWeapon
{
public:
    void describe()
    {
        cout << "This is a sword" << endl;
    };
    int getAttack()
    {
        return 10;
    };
};

class IWeaponDecorator : public IWeapon
{
};

class SuperSwordDecorator : public IWeaponDecorator
{
private:
    IWeapon *weapon;

public:
    SuperSwordDecorator(IWeapon *weapon)
    {
        this->weapon = weapon;
    }
    void describe()
    {
        cout << "This is an upgraded" << endl;
        weapon->describe();
    };
    int getAttack()
    {
        return 20 + weapon->getAttack();
    };
};

void testDecorator()
{
    IWeapon *sword = new Sword();
    sword->describe();
    cout << "Attack: " << sword->getAttack() << endl
         << endl;

    IWeapon *superSword = new SuperSwordDecorator(sword);
    superSword->describe();
    cout << "Attack: " << superSword->getAttack() << endl;
}

// as a client
int main(int argc, char *argv[])
{
    testDecorator();
    return 0;
}