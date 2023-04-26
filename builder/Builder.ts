
class Laptop {
    private cpu: string = "";
    private ram: string = "";
    private os: string = "";

    setCpu(cpu: string) {
        this.cpu = cpu;
    }

    setRam(ram: string) {
        this.ram = ram;
    }

    setOs(os: string) {
        this.os = os;
    }

    describe() {
        console.log("CPU: " + this.cpu);
        console.log("RAM: " + this.ram);
        console.log("OS: " + this.os);
    }
}

abstract class LaptopBuilder {
    public abstract setCpu(): void;
    public abstract setRam(): void;
    public abstract setOs(): void;
    public abstract build(): Laptop;
}

class HighPerformanceLaptopBuilder extends LaptopBuilder {
    private highPerformanceLaptop: Laptop = new Laptop();

    public setCpu() {
        this.highPerformanceLaptop.setCpu("i7 CPU");
    }

    public setRam() {
        this.highPerformanceLaptop.setRam("16GB RAM");
    }

    public setOs() {
        this.highPerformanceLaptop.setOs("Windows 10");
    }

    public build(): Laptop {
        return this.highPerformanceLaptop;
    }
}

class LowPerformanceLaptopBuilder extends LaptopBuilder {
    private lowPerformanceLaptop: Laptop = new Laptop();

    public setCpu() {
        this.lowPerformanceLaptop.setCpu("i3 CPU");
    }

    public setRam() {
        this.lowPerformanceLaptop.setRam("4GB RAM");
    }

    public setOs() {
        this.lowPerformanceLaptop.setOs("Windows 7");
    }

    public build(): Laptop {
        return this.lowPerformanceLaptop;
    }
}

class Director {
    private laptopBuilder: LaptopBuilder;

    public setLaptopBuilder(laptopBuilder: LaptopBuilder) {
        this.laptopBuilder = laptopBuilder;
    }

    public getLaptop(): Laptop {
        this.laptopBuilder.setCpu();
        this.laptopBuilder.setRam();
        this.laptopBuilder.setOs();
        return this.laptopBuilder.build();
    }
}

const testLaptopBuilder = () => {
    const director = new Director();
    const highPerformanceLaptopBuilder = new HighPerformanceLaptopBuilder();
    director.setLaptopBuilder(highPerformanceLaptopBuilder);
    const highPerformanceLaptop = director.getLaptop();
    console.log("High performance laptop:");
    highPerformanceLaptop.describe();

    const lowPerformanceLaptopBuilder = new LowPerformanceLaptopBuilder();
    director.setLaptopBuilder(lowPerformanceLaptopBuilder);
    const lowPerformanceLaptop = director.getLaptop();
    console.log("Low performance laptop:");
    lowPerformanceLaptop.describe();
}

testLaptopBuilder();