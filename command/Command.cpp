#include <iostream>
#include <string>

using namespace std;

class Light
{
public:
    void on()
    {
        cout << "Light is on" << endl;
    }
    void setBrightness(int brightness)
    {
        cout << "Light brightness is set to " << brightness << endl;
    }
    void off()
    {
        cout << "Light is off" << endl;
    }
};

class TV
{
public:
    void on()
    {
        cout << "TV is on" << endl;
    }
    void setChannel(int channel)
    {
        cout << "TV channel is set to " << channel << endl;
    }
    void off()
    {
        cout << "TV is off" << endl;
    }
};

class Fan
{
public:
    void on()
    {
        cout << "Fan is on" << endl;
    }
    void setSpeed(int speed)
    {
        cout << "Fan speed is set to " << speed << endl;
    }
    void off()
    {
        cout << "Fan is off" << endl;
    };
};

class Command
{
public:
    virtual void execute() = 0;
    virtual ~Command() {}
};

class LightOnCommand : public Command
{
private:
    Light *light;

public:
    LightOnCommand(Light *light)
    {
        this->light = light;
    }
    void execute()
    {
        light->on();
        light->setBrightness(100);
    }
};

class LightOffCommand : public Command
{
private:
    Light *light;

public:
    LightOffCommand(Light *light)
    {
        this->light = light;
    }
    void execute()
    {
        light->off();
    }
};

class TVOnCommand : public Command
{
private:
    TV *tv;

public:
    TVOnCommand(TV *tv)
    {
        this->tv = tv;
    }
    void execute()
    {
        tv->on();
        tv->setChannel(1);
    }
};

class TVOffCommand : public Command
{
private:
    TV *tv;

public:
    TVOffCommand(TV *tv)
    {
        this->tv = tv;
    }
    void execute()
    {
        tv->off();
    }
};

class FanOnCommand : public Command
{
private:
    Fan *fan;

public:
    FanOnCommand(Fan *fan)
    {
        this->fan = fan;
    }
    void execute()
    {
        fan->on();
        fan->setSpeed(3);
    }
};

class FanOffCommand : public Command
{
private:
    Fan *fan;

public:
    FanOffCommand(Fan *fan)
    {
        this->fan = fan;
    }
    void execute()
    {
        fan->off();
    }
};

class NoCommand : public Command
{
public:
    void execute()
    {
        cout << "No command" << endl;
    }
};

class Controller
{
private:
    Command **onCommandList;
    Command **offCommandList;
    const int MAX_COMMANDS = 5;

public:
    Controller()
    {
        onCommandList = new Command *[MAX_COMMANDS];
        offCommandList = new Command *[MAX_COMMANDS];
        for (int i = 0; i < MAX_COMMANDS; i++)
        {
            onCommandList[i] = new NoCommand();
            offCommandList[i] = new NoCommand();
        }
    }
    ~Controller()
    {
        delete[] onCommandList;
        delete[] offCommandList;
    }
    void setCommand(int slot, Command *onCommand, Command *offCommand)
    {
        onCommandList[slot] = onCommand;
        offCommandList[slot] = offCommand;
    }
    void onButtonWasPushed(int slot)
    {
        onCommandList[slot]->execute();
    }
    void offButtonWasPushed(int slot)
    {
        offCommandList[slot]->execute();
    }
};

// as a client
int main(int argc, char *argv[])
{
    TV *tv = new TV();
    Light *light = new Light();
    Fan *fan = new Fan();

    Controller *controller = new Controller();
    controller->setCommand(0, new TVOnCommand(tv), new TVOffCommand(tv));
    controller->setCommand(1, new LightOnCommand(light), new LightOffCommand(light));
    controller->setCommand(2, new FanOnCommand(fan), new FanOffCommand(fan));

    controller->onButtonWasPushed(0);
    controller->onButtonWasPushed(1);
    controller->onButtonWasPushed(2);
    // no command
    controller->onButtonWasPushed(3);

    controller->offButtonWasPushed(0);
    controller->offButtonWasPushed(1);
    controller->offButtonWasPushed(2);
    // no command
    controller->offButtonWasPushed(3);
}