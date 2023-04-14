#include <iostream>
#include <string>

using namespace std;

enum Material
{
    WOOD,
    STONE,
    IRON
};

// Abstract class as interface
class Axe
{
public:
    virtual string getMaterial() const = 0;
    virtual ~Axe() {}
};

class WoodAxe : public Axe
{
public:
    string getMaterial() const
    {
        return "Wood";
    }
    ~WoodAxe() {}
};

class StoneAxe : public Axe
{
public:
    string getMaterial() const
    {
        return "Stone";
    }
    ~StoneAxe() {}
};

class IronAxe : public Axe
{
public:
    string getMaterial() const
    {
        return "Iron";
    }
    ~IronAxe() {}
};

// Now we create an abstract factory, and a virtual function to create the axe
class AxeFactory
{
public:
    Axe virtual *createAxe(Material material) = 0;
    virtual ~AxeFactory() {}
};

// Now we create a wood axe factory, which will create the axe
class WoodAxeFactory : public AxeFactory
{
public:
    Axe *createAxe(Material material)
    {
        if (material == WOOD)
        {
            return new WoodAxe();
        }
        return NULL;
    }
};

class StoneAxeFactory : public AxeFactory
{
public:
    Axe *createAxe(Material material)
    {
        if (material == STONE)
        {
            return new StoneAxe();
        }
        return NULL;
    }
};

class IronAxeFactory : public AxeFactory
{
public:
    Axe *createAxe(Material material)
    {
        if (material == IRON)
        {
            return new IronAxe();
        }
        return NULL;
    }
};


void testAxeFactory()
{
    // Remeber to use pointers, because we are using polymorphism
    AxeFactory *factory;
    factory = new WoodAxeFactory();
    Axe *woodAxe = factory->createAxe(WOOD);
    delete factory;

    factory = new StoneAxeFactory();
    Axe *stoneAxe = factory->createAxe(STONE);
    delete factory;

    factory = new IronAxeFactory();
    Axe *ironAxe = factory->createAxe(IRON);
    delete factory;

    cout << "WoodAxe is made of " << woodAxe->getMaterial() << endl;
    cout << "StoneAxe is made of " << stoneAxe->getMaterial() << endl;
    cout << "IronAxe is made of " << ironAxe->getMaterial() << endl;

    delete woodAxe;
    delete stoneAxe;
    delete ironAxe;
}

int main(int argc, char *argv[])
{
    testAxeFactory();
    return 0;
}