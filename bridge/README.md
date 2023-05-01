# Bridge Pattern

Bridge is a structural design pattern that lets you split a large class or a set of closely related classes int to two separate hierarchies—abstraction and implementation—which can be developed independently of each other. For me, it is more likely a design mindset that avoid to use inheritance to solve the problem.

Let's looked at a simple idea. If we what to have a class can draw shape, such as circle and square, for us, we can simply design a class like this:

```java
public class ShapeDrawer {
    public void draw() {
        // ...
    }
}

public class CircleShapeDrawer extends ShapeDrawer {
    @Override
    public void draw() {
        // ...
    }
}

public class SquareShapeDrawer extends ShapeDrawer {
    @Override
    public void draw() {
        // ...
    }
}
```

Now, what if we want to draw the shape in different color? We can add a color parameter to the draw method, but it will make the code more complex. So, we can create a new class to solve this problem:

```java
public class RedCircleShapeDrawer extends CircleShapeDrawer {
    @Override
    public void draw() {
        // ...
    }
}

public class RedSquareShapeDrawer extends SquareShapeDrawer {
    @Override
    public void draw() {
        // ...
    }
}
```

We find a problem here, if we keep adding new shape or new color, we will have a lot of classes. How do we solve this problem?
As you can see, shape and drawer are two different concepts. Shape can store the information of shape, color, length and etc. On the other hand, drawer can draw the shape. So, we can separate the shape and shapedrawer into two different hierarchies.

```java
public interface Shape {
    void draw();
}

public class Drawer {
    protected Shape shape;

    public ShapeDrawer(Shape shape) {
        this.shape = shape;
    }

    public void drawShape() {
        shape.draw();
    };
}
```

Now, we can create a new shape.

```java
public class RedCircle implements Shape {
    @Override
    public void draw() {
        // ...
    }
}

public class RedSquare implements Shape {
    @Override
    public void draw() {
        // ...
    }
}
```

And client can control what to draw from the drawer.

```java

public static void main(String[] args) {
    Drawer redCircleDrawer = new Drawer( new RedCircle());
    Drawer redSquareDrawer = new Drawer(new RedSquare());

    redCircleDrawer.drawShape();
    redSquareDrawer.drawShape();
}
```

This pattern also imply a design principle that use composition over inheritance. Inheritance is a powerful tool, but it can make the code more complex. So, we should use composition to solve the problem if possible.