class USB_A():
    def USB_A_interface(self):
        print("USB-A interface")

class USB_C():
    def USB_C_interface(self):
        print("USB-C interface")

class USB_C_adapter(USB_C):
    def __init__(self, usb_a: USB_A):
        self.usb_a: USB_A = usb_a
    
    def USB_C_interface(self):
        print("Originally: ");
        self.usb_a.USB_A_interface()
        print("Now it's: ");
        print("USB-C interface")

class Macbook():
    def __init__(self, usb_c: USB_C):
        self.usb_c = usb_c
    
    def charge(self):
        self.usb_c.USB_C_interface()

# Client
if __name__ == "__main__":
    macbook = Macbook(USB_C_adapter(USB_A()))
    macbook.charge()