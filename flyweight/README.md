# Flyweight Method

Flyweight is a structural design pattern that prevents creation of multiple instances of a class with the same value by sharing the same object.

Let's look at an example. There is a multiplayer shooting game. In the game, system will generate millions of bullets. Each bullet has a position, direction, speed, and damage. If one bullte needs 32 bytes of memory, then 32,000,000 bullets will need 1GB of memory. The game will crash if the computer does not have enough memory. If we take a closer look at each bullet, we will find that most of the bullets are the same. They have the same position, direction, speed, and damage. The only difference is the position of the bullet. If we can share the same bullet object, we can save a lot of memory.

```java
public class Bullet {
    private int x;
    private int y;
    private int speed;
    private int damage;
    private String name;
}
```

We can group the speed, damage and name together and create a BulletType class. All the bullets will share the same BulletType object.

```java

public class BulletType {
    private int speed;
    private int damage;
    private String name;
    public BulletType(String name, int speed, int damage);
}

public class Bullet {
    private int x;
    private int y;
    private BulletType type;

}
```

We can manage a hashmap to keep track of all the BulletType objects. When we create a new bullet, we can check if the BulletType object already exists. If it does, we can reuse the object. If it does not, we can create a new one and add it to the hashmap.

```java

public class BulletFactory {
    private Map<String, BulletType> bulletTypes = new HashMap<>();

    public Bullet getBullet(String name, int x, int y) {
        BulletType type = bulletTypes.get(name);
        if (type == null) {
            type = new BulletType(name, 10, 10);
            bulletTypes.put(name, type);
        }
        return new Bullet(x, y, type);
    }
}
```

In the example above, we use the BulletFactory to create new bullets. The BulletFactory will check if the BulletType object already exists. If it does, it will reuse the object. If it does not, it will create a new one and add it to the hashmap.

```java

public static void main(String[] args) {
    BulletFactory factory = new BulletFactory();
    Bullet bullet1 = factory.getBullet("bullet1", 10, 10);
}
```

