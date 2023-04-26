from typing import Protocol


class Laptop():
    cpu: str
    ram: str
    os: str

    def __init__(self):
        self.cpu = ""
        self.ram = ""
        self.os = ""

    def setCpu(self, cpu: str):
        self.cpu = cpu

    def setRam(self, ram: str):
        self.ram = ram

    def setOs(self, os: str):
        self.os = os

    def describe(self):
        print("CPU: " + self.cpu)
        print("RAM: " + self.ram)
        print("OS: " + self.os)


class LaptopBuilder(Protocol):
    laptop: Laptop

    def setCpu(self):
        pass

    def setRam(self):
        pass

    def setOs(self):
        pass

    def build(self) -> Laptop:
        return self.laptop


class HighPerformanceLaptopBuilder(LaptopBuilder):
    laptop: Laptop

    def __init__(self):
        self.laptop = Laptop()

    def setCpu(self):
        self.laptop.setCpu("i7 CPU")

    def setRam(self):
        self.laptop.setRam("16GB RAM")

    def setOs(self):
        self.laptop.setOs("Windows 10")

    def build(self) -> Laptop:
        return self.laptop


class LowPerformanceLaptopBuilder(LaptopBuilder):
    laptop: Laptop

    def __init__(self):
        self.laptop = Laptop()

    def setCpu(self):
        self.laptop.setCpu("i3 CPU")

    def setRam(self):
        self.laptop.setRam("4GB RAM")

    def setOs(self):
        self.laptop.setOs("Windows 7")

    def build(self) -> Laptop:
        return self.laptop


class Director:
    laptopBuilder: LaptopBuilder

    def setLaptopBuilder(self, laptopBuilder: LaptopBuilder):
        self.laptopBuilder = laptopBuilder

    def getLaptop(self):
        self.laptopBuilder.setCpu()
        self.laptopBuilder.setRam()
        self.laptopBuilder.setOs()
        return self.laptopBuilder.build()


def testLaptopBuilder():
    director = Director()
    highPerformanceLaptopBuilder = HighPerformanceLaptopBuilder()
    director.setLaptopBuilder(highPerformanceLaptopBuilder)
    highPerformanceLaptop: Laptop = director.getLaptop()
    print("High performance laptop:")
    highPerformanceLaptop.describe()

    lowPerformanceLaptopBuilder = LowPerformanceLaptopBuilder()
    director.setLaptopBuilder(lowPerformanceLaptopBuilder)
    lowPerformanceLaptop = director.getLaptop()
    print("Low performance laptop:")
    lowPerformanceLaptop.describe()


if __name__ == "__main__":
    testLaptopBuilder()