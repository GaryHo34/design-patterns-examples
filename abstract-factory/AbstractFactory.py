from typing import Protocol

class Tool:
    def describe():
        pass
class Axe (Tool):
    pass

class Pickaxe (Tool):
    pass

class Shovel (Tool):
    pass

class WoodAxe(Axe):
    def describe(self):
        return "This is a wooden axe"
class StoneAxe(Axe):
    def describe(self):
        return "This is a stone axe"
class IronAxe(Axe):
    def describe(self):
        return "This is an iron axe"
    
class WoodPickaxe(Pickaxe):
    def describe(self):
        return "This is a wooden pickaxe"
class StonePickaxe(Pickaxe):
    def describe(self):
        return "This is a stone pickaxe"
class IronPickaxe(Pickaxe):
    def describe(self):
        return "This is an iron pickaxe"
    
class WoodShovel(Shovel):
    def describe(self):
        return "This is a wooden shovel"
class StoneShovel(Shovel):
    def describe(self):
        return "This is a stone shovel"
class IronShovel(Shovel):
    def describe(self):
        return "This is an iron shovel"

class ToolFactory(Protocol):
    def createAxe():
        pass
    def createPickaxe():
        pass
    def createShovel():
        pass

class WoodToolFactory(ToolFactory):
    def createAxe(self):
        return WoodAxe()
    def createPickaxe(self):
        return WoodPickaxe()
    def createShovel(self):
        return WoodShovel()
    
class StoneToolFactory(ToolFactory):
    def createAxe(self):
        return StoneAxe()
    def createPickaxe(self):
        return StonePickaxe()
    def createShovel(self):
        return StoneShovel()
    
class IronToolFactory(ToolFactory):
    def createAxe(self):
        return IronAxe()
    def createPickaxe(self):
        return IronPickaxe()
    def createShovel(self):
        return IronShovel()
    
class Client:
    def __init__(self, toolFactory: ToolFactory):
        self.toolFactory = toolFactory
    def testToolFactory(self):
        axe = self.toolFactory.createAxe()
        pickaxe = self.toolFactory.createPickaxe()
        shovel = self.toolFactory.createShovel()
        print(axe.describe())
        print(pickaxe.describe())
        print(shovel.describe())
        print()

if __name__ == "__main__":
    client = Client(WoodToolFactory())    
    client.testToolFactory()

    client = Client(StoneToolFactory())
    client.testToolFactory()

    client = Client(IronToolFactory())
    client.testToolFactory()
