# Builder Pattern

Builder Pattern is a creational design pattern that lets you construct complex objects step by step. The pattern define the process of constructing a complex object, but leaves the details of the construction process to be implemented by the class that implements the builder interface.

Let's take a look at a simple example, we have a `Laptop` class that has a lot of options. Depends on the CPU, RAM, OS and so on, we can produce different laptops. As a client of the `Laptop` class, we don't want to know how to build a laptop, we just want to get a laptop with the options we want. So we can use the builder pattern to build a laptop. By using `LaptopBuilder` class, client can easily get a laptop with the options they want.

```java
public class LaptopBuilder {
    private Laptop laptop;

    public void setCpu(String brand int core , int frequency) {
        laptop.setCpu(brand, core, frequency);
    }

    public void setRam(String ram) {
        laptop.setRam(ram);
    }

    public void setOs(String os) {
        laptop.setOs(os);
    }

    public Laptop build() {
        return laptop;
    }
}
```

The code above has a problem,we have to change the `LaptopBuilder` often to support different options. According to the Dependency Inversion Principle, we should depend on abstraction, not on concrete classes. We should make the `LaptopBuilder` class abstract and create concrete builder classes to support different options.

```java
public abstract class LaptopBuilder {
    public abstract void setCpu(String brand int core , int frequency);
    public abstract void setRam(String ram);
    public abstract void setOs(String os);
    public abstract Laptop build();
}

public class HighPerformanceLaptopBuilder extends LaptopBuilder {
    private Laptop highPerformanceLaptop;
    @Override
    public void setCpu(String cpu) {
        System.out.println("use Intel i7 CPU");
        laptop.setCpu(brand, core, frequency);
    }

    @Override
    public void setRam(String ram) {
        System.out.println("use 16GB RAM");
        laptop.setRam(ram);
    }

    @Override
    public void setOs(String os) {
        System.out.println("use Windows 10");
        laptop.setOs(os);
    }

    @Override
    public Laptop build() {
        return highPerformanceLaptop;
    }
}
```

Clients can choose the builder they want to build a laptop. But they have to call the methods in the right order. If they don't call the `setCpu` method, the laptop will not have a CPU. To solve this problem, we can use a `Director` class to control the order of the building process.

```java

public class Director {
    private LaptopBuilder laptopBuilder;

    public Director(LaptopBuilder laptopBuilder) {
        this.laptopBuilder = laptopBuilder;
    }

    public Laptop buildLaptop() {
        laptopBuilder.setCpu();
        laptopBuilder.setRam();
        laptopBuilder.setOs();
        return laptopBuilder.build();
    }
}
```

Now clients can use the `Director` class to build a laptop.

```java

public class Client {
    public static void main(String[] args) {
        // build a high performance laptop
        LaptopBuilder laptopBuilder = new HighPerformanceLaptopBuilder();
        Director director = new Director(laptopBuilder);
        Laptop laptop = director.buildLaptop();

        // build a low performance laptop
        LaptopBuilder laptopBuilder = new LowPerformanceLaptopBuilder();
        Director director = new Director(laptopBuilder);
        Laptop laptop = director.buildLaptop();
    }
}
```

The builder pattern is quite similar to the abstract factory pattern. The main difference is that the builder pattern focuses on constructing a complex object step by step, while the abstract factory pattern focuses on creating families of related objects. The builder pattern is often used to build a complex object, while the abstract factory pattern is often used to create a family of related objects.