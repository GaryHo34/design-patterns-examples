class BulletType:
    name: str
    speed: int
    damage: int

    def __init__(self, name, speed, damage):
        self.name = name
        self.speed = speed
        self.damage = damage


class Bullet:
    x: int
    y: int
    type: BulletType

    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

    def describe(self):
        print("Bullet " + self.type.name)
        print("Speed " + str(self.type.speed))
        print("Damage " + str(self.type.damage))
        print("@ (" + str(self.x) + ", " + str(self.y) + ")")


class BulletFactory:
    bulletTypes = {}

    def getBullet(self, name, x, y):
        type = self.bulletTypes.get(name)
        if type == None:
            type = BulletType(name, 10, 10)
            self.bulletTypes[name] = type
        return Bullet(x, y, type)


def testFlyweight():
    factory = BulletFactory()
    bullet1 = factory.getBullet("AK47", 0, 0)
    bullet2 = factory.getBullet("AK47", 0, 10)
    bullet1.describe()
    bullet2.describe()

    bullet3 = factory.getBullet("M4A1", 0, 10)
    bullet4 = factory.getBullet("M4A1", 0, 20)

    bullet3.describe()
    bullet4.describe()


if __name__ == "__main__":
    testFlyweight()
