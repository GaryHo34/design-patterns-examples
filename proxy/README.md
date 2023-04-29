# Proxy Pattern

Proxy is a structural design pattern that lets you provide a substitute or placeholder for another object. A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object.

To implement proxy pattern, we need to create an interface and concrete class that will implement the interface. Then we create a proxy class that will contain the object of concrete class and override all the methods of the interface. Then we call the methods of concrete class using reference variable of proxy class.

```java
public interface Image {
   void display();
}
```

The concrete class that implements Image interface. Note that it might take some time to load the image.

```java
public class RealImage implements Image {

    private String fileName;

    public RealImage(String fileName){
        this.fileName = fileName;
        loadFromDisk(fileName);
    }

    @Override
    public void display() {
        System.out.println("Displaying " + fileName);
    }

    private void loadFromDisk(String fileName){
        System.out.println("Loading " + fileName);
    }
}
```

To optimize the loading time, we are using the proxy pattern. The proxy pattern will create an object of RealImage class only if the image is not already present in the disk. Otherwise, it will just display the image from the disk.

```java
public class ProxyImage implements Image{

    private RealImage realImage;
    private String fileName;

    public ProxyImage(String fileName){
        this.fileName = fileName;
    }

    @Override
    public void display() {
        if(realImage == null){
            realImage = new RealImage(fileName);
        }
        realImage.display();
    }
}
```

ProxyPatternDemo, our demo class, will use ProxyImage to get an Image object to load and display as it needs.

```java
public class ProxyPatternDemo {

    public static void main(String[] args) {
        Image image = new ProxyImage("test_10mb.jpg");

        //image will be loaded from disk
        image.display();
        System.out.println("");

        //image will not be loaded from disk
        image.display();
    }
}
```
