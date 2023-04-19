public class Command {
    private class TV {
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

    private class Light {
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

    private class Fan {
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

    private interface ICommand {
        void execute();
    }

    private class TVOnCommand implements ICommand {
        private TV tv;

        public TVOnCommand(TV tv) {
            this.tv = tv;
        }

        @Override
        public void execute() {
            tv.on();
            tv.setChannel(5);
        }
    }

    private class TVOffCommand implements ICommand {
        private TV tv;

        public TVOffCommand(TV tv) {
            this.tv = tv;
        }

        @Override
        public void execute() {
            tv.off();
        }
    }

    private class LightOnCommand implements ICommand {
        private Light light;

        public LightOnCommand(Light light) {
            this.light = light;
        }

        @Override
        public void execute() {
            light.on();
            light.setLight(100);
            light.setTone(50);
        }
    }

    private class LightOffCommand implements ICommand {
        private Light light;

        public LightOffCommand(Light light) {
            this.light = light;
        }

        @Override
        public void execute() {
            light.off();
        }
    }

    private class FanOnCommand implements ICommand {
        private Fan fan;

        public FanOnCommand(Fan fan) {
            this.fan = fan;
        }

        @Override
        public void execute() {
            fan.on(3);
            fan.setSpeed(3);
        }
    }

    private class FanOffCommand implements ICommand {
        private Fan fan;

        public FanOffCommand(Fan fan) {
            this.fan = fan;
        }

        @Override
        public void execute() {
            fan.off();
        }
    }

    private class Controller {
        private ICommand[] onCommands;
        private ICommand[] offCommands;

        public Controller() {
            onCommands = new ICommand[3];
            offCommands = new ICommand[3];
        }

        public void setCommand(int slot, ICommand onCommand, ICommand offCommand) {
            onCommands[slot] = onCommand;
            offCommands[slot] = offCommand;
        }

        public void onButtonWasPushed(int slot) {
            onCommands[slot].execute();
        }

        public void offButtonWasPushed(int slot) {
            offCommands[slot].execute();
        }
    }

    public void testCommand() {
        Controller controller = new Controller();
        TV tv = new TV();
        Light light = new Light();
        Fan fan = new Fan();

        controller.setCommand(0, new TVOnCommand(tv), new TVOffCommand(tv));
        controller.setCommand(1, new LightOnCommand(light), new LightOffCommand(light));
        controller.setCommand(2, new FanOnCommand(fan), new FanOffCommand(fan));

        controller.onButtonWasPushed(0);
        controller.offButtonWasPushed(0);
        controller.onButtonWasPushed(1);
        controller.offButtonWasPushed(1);
        controller.onButtonWasPushed(2);
        controller.offButtonWasPushed(2);
    }

    public static void main(String[] args) {
        Command command = new Command();
        command.testCommand();
    }
}