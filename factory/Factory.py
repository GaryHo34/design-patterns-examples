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

class AxeFactory(Protocol):
    def createAxe(self, material: Material):
        pass

class WoodAxeFactory(AxeFactory):
    def createAxe(self, material: Material):
        if material == Material.WOOD:
            return WoodAxe()
        return None

class StoneAxeFactory(AxeFactory):
    def createAxe(self, material: Material):
        if material == Material.STONE:
            return StoneAxe()
        return None
    
class IronAxeFactory(AxeFactory):
    def createAxe(self, material: Material):
        if material == Material.IRON:
            return IronAxe()
        return None

def testAxeFactory():
    factory: AxeFactory = WoodAxeFactory()
    woodAxe = factory.createAxe(Material.WOOD)

    factory: AxeFactory = StoneAxeFactory()
    stoneAxe = factory.createAxe(Material.STONE)

    factory: AxeFactory = IronAxeFactory()
    ironAxe = factory.createAxe(Material.IRON)

    print("WoodAxe is made of " + woodAxe.getMaterial())
    print("StoneAxe is made of " + stoneAxe.getMaterial())
    print("IronAxe is made of " + ironAxe.getMaterial())

if __name__ == "__main__":
    testAxeFactory()
