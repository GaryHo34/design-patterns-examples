# Factory Method

Our crafting table can create three different axes, but what if we can create axes from more kind of matirials? We can add more casees to our switch statement, but it will be a mess. We can use factory method to solve this problem.

In the factory method, we abstract the creation of an object into a factory interface, and let the subclasses decide which class to instantiate. The factory method lets a class defer instantiation to subclasses.

Simply put, the class will be an abstract class, CraftingFactory, and the subclasses will be the actual factories, such as WoodenAxeFactory, StoneAxeFactory, and IronAxeFactory.

## Example

```java
public abstract class AxeFactory {
    // we defer the implementation of this method to subclasses
    public abstract Axe createAxe(Material material);
}

public class WoodenAxeFactory extends CraftingFactory {
    @Override
    public Axe createAxe(Material material) {
        return new WoodenAxe(material);
    }
}

public class StoneAxeFactory extends CraftingFactory {
    @Override
    public Axe createAxe(Material material) {
        return new StoneAxe(material);
    }
}

public class IronAxeFactory extends CraftingFactory {
    @Override
    public Axe createAxe(Material material) {
        return new IronAxe(material);
    }
}

```