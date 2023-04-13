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

// Factory class
class CraftingFactory
{
public:
    Axe *createAxe(Material material)
    {
        switch (material)
        {
        case WOOD:
            return new WoodAxe();
        case STONE:
            return new StoneAxe();
        case IRON:
            return new IronAxe();
        default:
            return nullptr;
        }
    }
};

void testCraftingFactory()
{
    CraftingFactory factory;
    Axe *woodAxe = factory.createAxe(WOOD);
    Axe *stoneAxe = factory.createAxe(STONE);
    Axe *ironAxe = factory.createAxe(IRON);

    cout << "WoodAxe is made of " << woodAxe->getMaterial() << endl;
    cout << "StoneAxe is made of " << stoneAxe->getMaterial() << endl;
    cout << "IronAxe is made of " << ironAxe->getMaterial() << endl;

    delete woodAxe;
    delete stoneAxe;
    delete ironAxe;
}

int main(int argc, char *argv[])
{
    testCraftingFactory();
    return 0;
}