#include <iostream>
#include <string>

using namespace std;

// Abstract class tool, api describe()
class Tool
{
public:
    virtual string describe() const = 0;
    virtual ~Tool() {}
};

// Axe is sublass of Tool
class Axe : public Tool
{
public:
    virtual ~Axe() {}
};

class Pickaxe : public Tool
{
public:
    virtual ~Pickaxe() {}
};

class Shovel : public Tool
{
public:
    virtual ~Shovel() {}
};

class WoodAxe : public Axe
{
public:
    string describe() const
    {
        return "This is a wooden axe";
    }
};

class StoneAxe : public Axe
{
public:
    string describe() const
    {
        return "This is a stone axe";
    }
};

class IronAxe : public Axe
{
public:
    string describe() const
    {
        return "This is a iron axe";
    }
};

class WoodPickaxe : public Pickaxe
{
public:
    string describe() const
    {
        return "This is a wooden pickaxe";
    }
};

class StonePickaxe : public Pickaxe
{
public:
    string describe() const
    {
        return "This is a stone pickaxe";
    }
};

class IronPickaxe : public Pickaxe
{
public:
    string describe() const
    {
        return "This is a iron pickaxe";
    }
};

class WoodShovel : public Shovel
{
public:
    string describe() const
    {
        return "This is a wooden shovel";
    }
};

class StoneShovel : public Shovel
{
public:
    string describe() const
    {
        return "This is a stone shovel";
    }
};

class IronShovel : public Shovel
{
public:
    string describe() const
    {
        return "This is a iron shovel";
    }
};

// Abstract factory

class ToolFactory
{ // Abstract factory
public:
    virtual Axe *createAxe() const = 0;
    virtual Pickaxe *createPickaxe() const = 0;
    virtual Shovel *createShovel() const = 0;
    virtual ~ToolFactory() {}
};

class WoodToolFactory : public ToolFactory
{
public:
    Axe *createAxe() const
    {
        return new WoodAxe();
    }
    Pickaxe *createPickaxe() const
    {
        return new WoodPickaxe();
    }
    Shovel *createShovel() const
    {
        return new WoodShovel();
    }
};

class StoneToolFactory : public ToolFactory
{
public:
    Axe *createAxe() const
    {
        return new StoneAxe();
    }
    Pickaxe *createPickaxe() const
    {
        return new StonePickaxe();
    }
    Shovel *createShovel() const
    {
        return new StoneShovel();
    }
};

class IronToolFactory : public ToolFactory
{
public:
    Axe *createAxe() const
    {
        return new IronAxe();
    }
    Pickaxe *createPickaxe() const
    {
        return new IronPickaxe();
    }
    Shovel *createShovel() const
    {
        return new IronShovel();
    }
};

class Client
{
    ToolFactory *factory;

public:
    Client(ToolFactory *factory)
    {
        this->factory = factory;
    }
    ~Client()
    {
        delete factory;
    }

    void testToolFactory()
    {
        Axe *axe = factory->createAxe();
        Pickaxe *pickaxe = factory->createPickaxe();
        Shovel *shovel = factory->createShovel();

        cout << axe->describe() << endl;
        cout << pickaxe->describe() << endl;
        cout << shovel->describe() << endl
             << endl;

        delete axe;
        delete pickaxe;
        delete shovel;
    }
};

int main(int argc, char *argv[])
{
    Client *client = new Client(new WoodToolFactory());
    client->testToolFactory();
    delete client;

    client = new Client(new StoneToolFactory());
    client->testToolFactory();
    delete client;

    client = new Client(new IronToolFactory());
    client->testToolFactory();
    delete client;

    return 0;
}