from typing import Protocol

class IWeapon(Protocol):
    def describe():
        pass
    def getAttack()->int:
        pass

class Sword(IWeapon):
    def describe(self):
        print("This is a sword")
    def getAttack(self)->int:
        return 10

class IWeaponDecorator(IWeapon):
    pass

class SuperSwordDecorator(IWeaponDecorator):
    def __init__(self, weapon:IWeapon):
        self.weapon = weapon
    def describe(self):
        print("This is a super version")
        self.weapon.describe()
    def getAttack(self)->int:
        return self.weapon.getAttack() + 20
    
def testDecorator():
    sword = Sword()
    sword.describe()
    print("Attack:", sword.getAttack())
    superSword = SuperSwordDecorator(sword)
    superSword.describe()
    print("Attack:", superSword.getAttack())

if __name__ == "__main__":
    testDecorator()