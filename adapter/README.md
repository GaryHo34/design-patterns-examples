# Adapter Pattern

Adapter Pattern is a structural design pattern that allows objects with incompatible interfaces to collaborate.

Let take USB-C as an example. USB-C has been adapted as a standard for charging and data transfer. However, it is not compatible with the previous USB standard. Some devices, such as macbook, have only USB-C ports. If you want to connect a USB-C device to a USB-A device, you need an adapter.

We have a device only can injected a USB-C class, but we want to use it with a USB-A class. So we create a adapter class, which extends from USB-C but can be injected with USB-A. We implement USB-C interface in the adapter class, and use USB-A class in the adapter class.

```java

public class USB_A {
    void USB_A_interface() {
        System.out.println("USB-C interface");
    }
}
        
public class USB_C {
    void USB_C_interface() {
        System.out.println("USB-C interface");
    }
}

public class USB_C_Adapter extends USB_C {
    private USB_A usb_a;
    public USB_C_Adapter(USB_A usb_a) {
        this.usb_a = usb_a;
    }
    @Override
    void USB_C_interface() {
        // do something here
        System.out.println("Now it's USB-C interface!");
    }
}

public class Macbook {
    private USB_C usb_c;
    public Macbook(USB_C usb_c) {
        this.usb_c = usb_c;
    }
    void charge() {
        usb_c.USB_C_interface();
    }
}

public class client {
    public static void main(String[] args) {
        Macbook macbook = new Macbook(new USB_C_Adapter(new USB_A()));
        macbook.charge();
    }
}
```
