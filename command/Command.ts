class TV {
    on() {
        console.log("TV is on");
    }
    setChannel(channel: number) {
        console.log("Channel is set to " + channel);
    }
    off() {
        console.log("TV is off");
    }
}

class Light {
    on() {
        console.log("Light is on");
    }
    setBrightness(brightness: number) {
        console.log("Brightness is set to " + brightness);
    }
    off() {
        console.log("Light is off");
    }
}

class Fan {
    on() {
        console.log("Fan is on");
    }
    setSpeed(speed: number) {
        console.log("Speed is set to " + speed);
    }
    off() {
        console.log("Fan is off");
    }
}

interface Command {
    execute(): void;
}

class TVOnCommand implements Command {
    private tv: TV;
    constructor(tv: TV) {
        this.tv = tv;
    }
    execute() {
        this.tv.on();
        this.tv.setChannel(1);
    }
}

class TVOffCommand implements Command {
    private tv: TV;
    constructor(tv: TV) {
        this.tv = tv;
    }
    execute() {
        this.tv.off();
    }
}

class LightOnCommand implements Command {
    private light: Light;
    constructor(light: Light) {
        this.light = light;
    }
    execute() {
        this.light.on();
        this.light.setBrightness(100);
    }
}

class LightOffCommand implements Command {
    private light: Light;
    constructor(light: Light) {
        this.light = light;
    }
    execute() {
        this.light.off();
    }
}

class FanOnCommand implements Command {
    private fan: Fan;
    constructor(fan: Fan) {
        this.fan = fan;
    }
    execute() {
        this.fan.on();
        this.fan.setSpeed(100);
    }
}

class FanOffCommand implements Command {
    private fan: Fan;
    constructor(fan: Fan) {
        this.fan = fan;
    }
    execute() {
        this.fan.off();
    }
}
class NoCommand implements Command {
    constructor() { }
    execute() {
        console.log("No command");
    }
}

class RemoteControl {
    private onCommands: Command[];
    private offCommands: Command[];
    private readonly MAX_SLOTS: number = 5;
    constructor() {
        this.onCommands = new Array<Command>(this.MAX_SLOTS);
        this.offCommands = new Array<Command>(this.MAX_SLOTS);
        for (let i = 0; i < this.MAX_SLOTS; i++) {
            this.onCommands[i] = new NoCommand();
            this.offCommands[i] = new NoCommand();
        }
    }
    setCommand(slot: number, onCommand?: Command, offCommand?: Command) {
        if (slot < 0 || slot >= this.MAX_SLOTS) {
            throw new Error("Invalid slot");
        }
        if (!!onCommand)
            this.onCommands[slot] = onCommand;
        if (!!offCommand)
            this.offCommands[slot] = offCommand;
    }
    onButtonWasPushed(slot: number) {
        if (slot < 0 || slot >= this.MAX_SLOTS) {
            throw new Error("Invalid slot");
        }
        this.onCommands[slot].execute();
    }
    offButtonWasPushed(slot: number) {
        if (slot < 0 || slot >= this.MAX_SLOTS) {
            throw new Error("Invalid slot");
        }
        this.offCommands[slot].execute();
    }
}

function testController() {
    const tv: TV = new TV();
    const light: Light = new Light();
    const fan: Fan = new Fan();
    const remoteControl: RemoteControl = new RemoteControl();
    remoteControl.setCommand(0, new TVOnCommand(tv), new TVOffCommand(tv));
    remoteControl.setCommand(1, new LightOnCommand(light), new LightOffCommand(light));
    remoteControl.setCommand(2, new FanOnCommand(fan), new FanOffCommand(fan));

    remoteControl.onButtonWasPushed(0);
    remoteControl.offButtonWasPushed(0);
    remoteControl.onButtonWasPushed(1);
    remoteControl.offButtonWasPushed(1);
    remoteControl.onButtonWasPushed(2);
    remoteControl.offButtonWasPushed(2);
    // Try no command
    remoteControl.onButtonWasPushed(3);
    remoteControl.offButtonWasPushed(3);
}

testController();