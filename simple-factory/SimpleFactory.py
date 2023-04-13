from enum import Enum
# python 3.8 and above
from typing import Protocol, Dict

class Material(Enum):
    WOOD = 1
    STONE = 2
    IRON = 3

# protocol is a new feature in python 3.8, it is similar to interface in java
# Note that it is only for type checking, it does not enforce the implementation
# https://docs.python.org/3/library/typing.html#typing.Protocol

class Axe(Protocol):
    def getMaterial(self):
        pass

class WoodAxe(Axe):
    def getMaterial(self):
        return "wood"

class StoneAxe(Axe):
    def getMaterial(self):
        return "stone"

class IronAxe(Axe):
    def getMaterial(self):
        return "iron"

class CraftingFactory:
    def createAxe(self, material: Material):
        craftMap: Dict[Material, Axe] = {
            Material.WOOD: WoodAxe,
            Material.STONE: StoneAxe,
            Material.IRON: IronAxe
        }
        if(material not in craftMap):
            raise Exception("Invalid material")
        return craftMap[material]()

def testCraftingFactory():
    factory = CraftingFactory()
    woodAxe = factory.createAxe(Material.WOOD)
    stoneAxe = factory.createAxe(Material.STONE)
    ironAxe = factory.createAxe(Material.IRON)

    print("WoodAxe is made of " + woodAxe.getMaterial())
    print("StoneAxe is made of " + stoneAxe.getMaterial())
    print("IronAxe is made of " + ironAxe.getMaterial())

if __name__ == "__main__":
    testCraftingFactory()
