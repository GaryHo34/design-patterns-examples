// Adapter/USB_A.ts
class USB_A {
    USB_A_interface(): void {
        console.log("USB-A interface");
    }
}

// Adapter/USB_C.ts
class USB_C {
    USB_C_interface(): void {
        console.log("USB-C interface");
    }
}

// Adapter/USB_C_adapter.ts
class USB_C_adapter extends USB_C {
    private usb_a: USB_A;

    constructor(usb_a: USB_A) {
        super();
        this.usb_a = usb_a;
    }

    USB_C_interface(): void {
        console.log("Originally: ");
        this.usb_a.USB_A_interface();
        console.log("Now it's: ");
        console.log("USB-C interface");
    }
}

class Macbook {
    private usb_c: USB_C;

    constructor(usb_c: USB_C) {
        this.usb_c = usb_c;
    }

    charge(): void {
        this.usb_c.USB_C_interface();
    }
}

// Client
const macbook = new Macbook(new USB_C_adapter(new USB_A()));
macbook.charge();