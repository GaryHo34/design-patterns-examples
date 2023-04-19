from typing import Protocol, Optional

class TV:
    def on(self):
        print("TV is on")
    def setChannel(self, channel: int):
        print("Channel is set to ", channel)
    def turn_off(self):
        print("TV is off")

class Light:
    def on(self):
        print("Light is on")
    def setBrightness(self, brightness: int):
        print("Brightness is set to ", brightness)
    def setTone(self, tone: int):
        print("Tone is set to " , tone)
    def off(self):
        print("Light is off")

class Fan:
    def on(self):
        print("Fan is on")
    def setSpeed(self, speed: int):
        print("Speed is set to ", speed)
    def off(self):
        print("Fan is off")

class Command(Protocol):
    def execute(self):
        pass

class TVOnCommand:
    def __init__(self, tv: TV):
        self.tv = tv
    def execute(self):
        self.tv.on()
        self.tv.setChannel(1)

class TVOffCommand:
    def __init__(self, tv: TV):
        self.tv = tv
    def execute(self):
        self.tv.turn_off()

class LightOnCommand:
    def __init__(self, light: Light):
        self.light = light
    def execute(self):
        self.light.on()
        self.light.setBrightness(100)
        self.light.setTone(50)

class LightOffCommand:
    def __init__(self, light: Light):
        self.light = light
    def execute(self):
        self.light.off()

class FanOnCommand:
    def __init__(self, fan: Fan):
        self.fan = fan
    def execute(self):
        self.fan.on()
        self.fan.setSpeed(3)

class FanOffCommand:
    def __init__(self, fan: Fan):
        self.fan = fan
    def execute(self):
        self.fan.off()
class NoCommand:
    def execute(self):
        print("No command")

class RemoteController:
    def __init__(cls):
        cls.MAX_COMMANDS = 5
        cls.onCommands = [NoCommand() for _ in range(cls.MAX_COMMANDS)]
        cls.offCommands = [NoCommand() for _ in range(cls.MAX_COMMANDS)]
    
    def setCommand(self,slot:int, onCommand:Optional[Command], offCommand:Optional[Command]):
        if slot < 0 or slot >= self.MAX_COMMANDS:
            print("Invalid slot")
            return
        if onCommand:
            self.onCommands[slot] = onCommand
        if offCommand:
            self.offCommands[slot] = offCommand
    def onButtonWasPressed(self, slot: int):
        if slot < 0 or slot >= self.MAX_COMMANDS:
            print("Invalid slot")
            return
        self.onCommands[slot].execute()

    def offButtonWasPressed(self, slot: int):
        if slot < 0 or slot >= self.MAX_COMMANDS:
            print("Invalid slot")
            return
        self.offCommands[slot].execute()


# Client
if __name__ == "__main__":
    tv: TV = TV()
    light: Light = Light()
    fan: Fan = Fan()

    tvOnCommand: Command = TVOnCommand(tv)
    tvOffCommand: Command = TVOffCommand(tv)
    lightOnCommand: Command = LightOnCommand(light)
    lightOffCommand: Command = LightOffCommand(light)
    fanOnCommand: Command = FanOnCommand(fan)
    fanOffCommand: Command = FanOffCommand(fan)

    remoteController: RemoteController = RemoteController()
    remoteController.setCommand(0, tvOnCommand, tvOffCommand)
    remoteController.setCommand(1, lightOnCommand, lightOffCommand)
    remoteController.setCommand(2, fanOnCommand, fanOffCommand)

    remoteController.onButtonWasPressed(0)
    remoteController.offButtonWasPressed(0)
    remoteController.onButtonWasPressed(1)
    remoteController.offButtonWasPressed(1)
    remoteController.onButtonWasPressed(2)
    remoteController.offButtonWasPressed(2)
    # Try no command
    remoteController.onButtonWasPressed(3)
    remoteController.offButtonWasPressed(3)