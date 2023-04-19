# Command Pattern

Command Pattern is a behavioral design pattern that turns a request into a stand-alone object that contains all information about the request. This transformation lets you parameterize methods with different requests, delay or queue a request’s execution, and support undoable operations.

If we are desiging a smart controll system which allows us to control the light, fan, and TV all in one class, but every appliance has its own on and off method. The code will be quite messy and hard to maintain.

```java
public class TV {
    public void on() {
        System.out.println("TV is on");
    }
    
    public void setChannel(int channel) {
        System.out.println("TV is on with channel " + channel);
    }

    public void off() {
        System.out.println("TV is off");
    }
}

public class Light {
    public void on() {
        System.out.println("Light is on");
    }
    
    public void setLight(int brightness) {
        System.out.println("Light is on with brightness " + brightness);
    }

    public void setTone(int tone) {
        System.out.println("Light is on with tone " + tone);
    }

    public void off() {
        System.out.println("Light is off");
    }
}

public class Fan {
    public void on(int speed) {
        System.out.println("Fan is on with speed " + speed);
    }

    public void setSpeed(int speed) {
        System.out.println("Fan is on with speed " + speed);
    }

    public void off() {
        System.out.println("Fan is off");
    }
}

public class Controller {
    private TV tv;
    private Light light;
    private Fan fan;

    public Controller(TV tv, Light light, Fan fan) {
        this.tv = tv;
        this.light = light;
        this.fan = fan;
    }

    public void on() {
        tv.on();
        tv.setChannel(3);
        light.on();
        light.setLight(100);
        fan.on(3);
        fan.setSpeed(3);
    }
}
```

The command pattern is a solution to this problem. It allows us to encapsulate the request as an object, thereby letting us parameterize other objects with different requests, queue or log requests, and support undoable operations.

We encapsulate the real object in a command object, and then pass the command object to the invoker. The invoker will call the execute method of the command object, and the command object will call the corresponding method of the real object.

```java

public interface Command {
    void execute();
}

public class TVOnCommand implements Command {
    private TV tv;

    public TVOnCommand(TV tv) {
        this.tv = tv;
    }

    @Override
    public void execute() {
        tv.on();
        tv.setChannel(3);
    }
}

public class LightCommand implements Command {
    private Light light;

    public LightCommand(Light light) {
        this.light = light;
    }

    @Override
    public void execute() {
        light.on();
        light.setLight(100);        
    }
}

public class FanCommand implements Command {
    private Fan fan;

    public FanCommand(Fan fan) {
        this.fan = fan;
    }

    @Override
    public void execute() {
        fan.on(3);
        fan.setSpeed(3);
    }
}

// We also design a NoCommand class to handle the case when the user does not specify a command.

public class NoCommand implements Command {
    @Override
    public void execute() {
        System.out.println("No command");
    }

    @Override
    public void undo() {
        System.out.println("No command");
    }
}

// The controller is totally decoupled from the real object.

public class Controller {
    private const int NUM_OF_SLOTS = 10;
    private Command[] onCommands;

    public Controller() {
        onCommands = new Command[NUM_OF_SLOTS];
        for (int i = 0; i < 3; i++) {
            onCommands[i] = new NoCommand();
        }
    }

    public void setOnCommand(int index, Command onCommand) {
        onCommands[index] = onCommand;
    }

    public void onButtonWasPushed(int slot) {
        onCommands[slot].execute();
    }
}

public class Client {
    public static void main(String[] args) {
        TV tv = new TV();
        Light light = new Light();
        Fan fan = new Fan();
        Controller controller = new Controller();

        controller.setOnCommand(0, new TVOnCommand(tv));
        controller.setOnCommand(1, new LightCommand(light));
        controller.setOnCommand(2, new FanCommand(fan));

        controller.onButtonWasPushed(0);
        controller.onButtonWasPushed(1);
        controller.onButtonWasPushed(2);
    }
}
```

