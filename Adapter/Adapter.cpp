#include <iostream>
#include <string>

using namespace std;

class USB_A
{
public:
    virtual void USB_A_interface()
    {
        cout << "USB-A interface" << endl;
    };
};

class USB_C
{
public:
    virtual void USB_C_interface()
    {
        cout << "USB-C interface" << endl;
    };
};

class USB_C_Adapter : public USB_C
{
private:
    USB_A *usb_a;
public:
    USB_C_Adapter(USB_A *usb_a)
    {
        this->usb_a = usb_a;
    }
    void USB_C_interface()
    {
        cout << "Original: " << endl;
        usb_a->USB_A_interface();
        cout << "After adapter: " << endl;
        cout << "USB-C interface" << endl;
    }
};

class Macbook {
private:
    USB_C *usb_c;
public:
    Macbook(USB_C *usb_c)
    {
        this->usb_c = usb_c;
    }
    void charge()
    {
        usb_c->USB_C_interface();
    }
};

// as a client
int main(int argc, char *argv[])
{
    Macbook *mb = new Macbook(new USB_C_Adapter(new USB_A()));
    mb->charge();
    return 0;
}