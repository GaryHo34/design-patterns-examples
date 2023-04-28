class BulletType {
    speed: number;
    damage: number;
    name: string;

    constructor(name: string, speed: number, damage: number) {
        this.name = name;
        this.speed = speed;
        this.damage = damage;
    }
}

class Bullet {
    x: number;
    y: number;
    type: BulletType;

    constructor(x: number, y: number, type: BulletType) {
        this.x = x;
        this.y = y;
        this.type = type;
    }

    describe() {
        console.log(`Bullet ${this.type.name}`);
        console.log(`Speed ${this.type.speed}`);
        console.log(`Damage ${this.type.damage}`);
        console.log(`@ (${this.x}, ${this.y})`);
    }
}

class BulletFactory {
    bulletTypes: Map<string, BulletType> = new Map();

    getBullet(name: string, x: number, y: number) {
        let type = this.bulletTypes.get(name);
        if (!type) {
            type = new BulletType(name, 10, 10);
            this.bulletTypes.set(name, type);
        }
        return new Bullet(x, y, type);
    }
}

function testFlyweight() {
    const factory = new BulletFactory();
    const bullet1 = factory.getBullet("AK47", 0, 0);
    const bullet2 = factory.getBullet("AK47", 0, 10);
    bullet1.describe();
    bullet2.describe();

    const bullet3 = factory.getBullet("M4A1", 0, 10);
    const bullet4 = factory.getBullet("M4A1", 0, 20);

    bullet3.describe();
    bullet4.describe();
}

testFlyweight();