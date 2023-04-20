# Decorator Pattern

Decorator pattern is a structural design pattern that allows behavior to be added to an individual object, either statically or dynamically, without affecting the behavior of other objects from the same class.

If you have played any MMO RPG, you will notice that a character can wear equipments and hold weapons. In the mean while those equipments and weapons can be upgraded. Here comes the problem, how do we implement the upgrade of equipments and weapons? 

The naive idea would be create a new class for any upgrade of equipments and weapons. For example, if we have a sword, and we want to upgrade it to a better sword, we can create a new class called `BetterSword` and inherit from `Sword`. Then we can override the `attack` method of `Sword` to implement the new attack behavior. 

```java

public interface Weapon {
    void describe();
    int getAttack();
}

public class Sword implements Weapon {
    @Override
    public void describe() {
        System.out.println("This is a sword");
    }

    @Override
    public int getAttack() {
        return 10;
    }
}

public class BetterSword extends Sword {
    @Override
    public void describe() {
        System.out.println("This is a better sword");
    }

    @Override
    public int getAttack() {
        return super.getAttack() + 10;
    }
}
```

But this approach has a big problem. If we want to upgrade the sword to a super sword, we have to create a new class called `SuperSword` and inherit from `BetterSword`. Then we have to override the `attack` method of `BetterSword` to implement the new attack behavior. Thousands of classes will be created if we have multiple ways to upgrade different equipments and weapons. 

The decorator pattern is a solution to this problem. It allows behavior to be added to an individual object, either statically or dynamically, without affecting the behavior of other objects from the same class.

We can create a decorator class extends the abstract class, and override the methods we want to decorate. Then we can create a new instance of the decorator class and pass the instance of the abstract class to the constructor of the decorator class. 

Note that the decorator class and the class we want to decorate should have the same interface and same parent class. 

```java
public abstract class WeaponDecorator implements Weapon {
    protected Weapon weapon;

    public WeaponDecorator(Weapon weapon) {
        this.weapon = weapon;
    }

    @Override
    public void describe() {
        weapon.describe();
    }

    @Override
    public int getAttack() {
        return weapon.getAttack();
    }
}

public class superSword extends WeaponDecorator {
    protected weapon;

    public superSword(Weapon weapon) {
        this.weapon = weapon;
    }

    @Override
    public void describe() {
        super.describe();
        System.out.println("This is a super sword");
    }

    @Override
    public int getAttack() {
        return super.getAttack() + 20;
    }
}
```

Then we can create a new instance of the decorator class and pass the instance of the abstract class to the constructor of the decorator class. 

```java
public class Main {
    public static void main(String[] args) {
        Weapon weapon = new Sword();
        weapon.describe();
        System.out.println("Attack: " + weapon.getAttack());

        weapon = new BetterSword(weapon);
        weapon.describe();
        System.out.println("Attack: " + weapon.getAttack());

        weapon = new SuperSword(weapon);
        weapon.describe();
        System.out.println("Attack: " + weapon.getAttack());
    }
}
```