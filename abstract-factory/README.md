# Abstract Factory Method

Now, we defined the factory method pattern. However, if we want to create other tools, such as pickaxes or shovels, we need to create a new factory method for each tool. This is not ideal, because we want to hide the implementation details from the client. We can do this by using the abstract factory pattern.

As a client, the only thing we need to know is that, we have a factory instance and we can invoke the corresponding method to create the tool we want. We don't need to know the implementation details of the factory.

So, we can define an abstract factory class, which contains the factory method for creating tools. Then, we can create subclasses of the abstract factory class, which implement the factory method for creating tools. The client can use the factory method to create tools.

Note that application should decide which concrete factory to use, and pass it to the client. The client should not be responsible for creating the concrete factory.

## Example code

```java
public abstract class ToolFactory {
    public abstract Axe createAxe(Material material);
    public abstract Pickaxe createPickaxe(Material material);
    public abstract Shovel createShovel(Material material);
}

public class WoodToolFactory extends ToolFactory {
    @Override
    public Axe createAxe(Material material) {
        return new WoodAxe(material);
    }

    @Override
    public Pickaxe createPickaxe(Material material) {
        return new WoodPickaxe(material);
    }

    @Override
    public Shovel createShovel(Material material) {
        return new WoodShovel(material);
    }
}

public class Client {
    private ToolFactory factory;

    public Client(ToolFactory factory) {
        this.factory = factory;
    }

    public static void main(String[] args) {
        ToolFactory factory = new WoodToolFactory();
        Client client = new Client(factory);

        // as a client, we only know what api we can use
        client.createAxe();
        client.createPickaxe();
        client.createShovel();
    }
}

```