# Simple Factory

The simple factory pattern is a creational pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

A single factory usually handles the creation of objects from a single product family. It is called simple because it only creates objects, without having to specify the exact class of the object that will be created.

## Example code

Let's take minecraft as an example, we can create an axe from different materials, such as woods, stones, and metals. The crafting table is a simple factory that can create different axes from different materials.

```java
public class CraftingFactory {
    
    public static Axe createAxe(Material material) {
        switch (material) {
            case WOOD:
                return new WoodenAxe();
            case STONE:
                return new StoneAxe();
            case IRON:
                return new IronAxe();
            default:
                throw new IllegalArgumentException("Invalid material");
        }
    }
}

```