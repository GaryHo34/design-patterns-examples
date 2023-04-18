public class Adapter {
    private class USB_A {
        public void USB_A_interface() {
            System.out.println("USB-A interface");
        }
    }

    private class USB_C {
        public void USB_C_interface() {
            System.out.println("USB-C interface");
        }
    }
    
    private class USB_C_Adapter extends USB_C {
        private USB_A usb_a;

        public USB_C_Adapter(USB_A usb_a) {
            this.usb_a = usb_a;
        }
        
        @Override
        public void USB_C_interface() {
            // do something here
            System.out.print("Originally: ");
            usb_a.USB_A_interface();
            System.out.println("Now it's USB-C interface!");
        }
    }
    
    private class Macbook {
        private USB_C usb_c;
        public Macbook(USB_C usb_c) {
            this.usb_c = usb_c;
        }
        void charge() {
            usb_c.USB_C_interface();
        }
    }
    
    public void testAdapter() {
        Macbook macbook = new Macbook(new USB_C_Adapter(new USB_A()));
        macbook.charge();
    }
    

    public static void main(String[] args) {
        Adapter adapter = new Adapter();
        adapter.testAdapter();
    }
}