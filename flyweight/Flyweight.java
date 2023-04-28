import java.util.HashMap;

public class Flyweight {

    private class BulletType {
        private int speed;
        private int damage;
        private String name;

        public BulletType(String name, int speed, int damage) {
            this.name = name;
            this.speed = speed;
            this.damage = damage;
        }
    }

    private class Bullet {
        private int x;
        private int y;
        private BulletType type;

        public Bullet(int x, int y, BulletType type) {
            this.x = x;
            this.y = y;
            this.type = type;
        }

        public void describe() {
            System.out.println("Bullet " + type.name);  
            System.out.println("Speed " + this.type.speed);
            System.out.println("Damage " + this.type.damage);
            System.out.println("@ (" + x + ", " + y + ")");
        }
    }

    private class BulletFactory {
        private HashMap<String, BulletType> bulletTypes = new HashMap<>();

        public Bullet getBullet(String name, int x, int y) {
            BulletType type = bulletTypes.get(name);
            if (type == null) {
                type = new BulletType(name, 10, 10);
                bulletTypes.put(name, type);
            }
            return new Bullet(x, y, type);
        }
    }

    public void testFlyweight() {
        BulletFactory factory = new BulletFactory();
        Bullet bullet1 = factory.getBullet("AK47", 0, 0);
        Bullet bullet2 = factory.getBullet("AK47", 0, 10);
        bullet1.describe();
        System.out.println("JESFA");
        bullet2.describe();

        Bullet bullet3 = factory.getBullet("M4A1", 0, 10);
        Bullet bullet4 = factory.getBullet("M4A1", 0, 20);

        bullet3.describe();
        bullet4.describe();
    }

    public static void main(String[] args) {
        Flyweight flyweight = new Flyweight();
        flyweight.testFlyweight();
    }
}