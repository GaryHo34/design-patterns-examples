#include <iostream>
#include <string>

using namespace std;

class Laptop {
    private:
        string cpu;
        string ram;
        string os;
    public:
        void setCpu(string cpu) {
            this->cpu = cpu;
        }
        void setRam(string ram) {
            this->ram = ram;
        }
        void setOs(string os) {
            this->os = os;
        }
        void describe() {
            cout << "CPU: " << cpu << endl;
            cout << "RAM: " << ram << endl;
            cout << "OS: " << os << endl;
        }
};

class LaptopBuilder {
    public:
        virtual void setCpu() = 0;
        virtual void setRam() = 0;
        virtual void setOs() = 0;
        virtual Laptop* build() = 0;
};

class HighPerformanceLaptopBuilder : public LaptopBuilder {
    private:
        Laptop* highPerformanceLaptop;
    public:
        HighPerformanceLaptopBuilder() {
            highPerformanceLaptop = new Laptop();
        }
        void setCpu() {
            highPerformanceLaptop->setCpu("i7 CPU");
        }
        void setRam() {
            highPerformanceLaptop->setRam("16GB RAM");
        }
        void setOs() {
            highPerformanceLaptop->setOs("Windows 10");
        }
        Laptop* build() {
            return highPerformanceLaptop;
        }
};

class LowPerformanceLaptopBuilder : public LaptopBuilder {
    private:
        Laptop* lowPerformanceLaptop;
    public:
        LowPerformanceLaptopBuilder() {
            lowPerformanceLaptop = new Laptop();
        }
        void setCpu() {
            lowPerformanceLaptop->setCpu("i3 CPU");
        }
        void setRam() {
            lowPerformanceLaptop->setRam("4GB RAM");
        }
        void setOs() {
            lowPerformanceLaptop->setOs("Windows 7");
        }
        Laptop* build() {
            return lowPerformanceLaptop;
        }
};

class Director {
    private:
        LaptopBuilder* laptopBuilder;
    public:
        void setLaptopBuilder(LaptopBuilder* laptopBuilder) {
            this->laptopBuilder = laptopBuilder;
        }
        Laptop* getLaptop() {
            laptopBuilder->setCpu();
            laptopBuilder->setRam();
            laptopBuilder->setOs();
            return laptopBuilder->build();
        }
};

int main() {
    Director* director = new Director();
    LaptopBuilder* highPerformanceLaptopBuilder = new HighPerformanceLaptopBuilder();
    director->setLaptopBuilder(highPerformanceLaptopBuilder);
    Laptop* highPerformanceLaptop = director->getLaptop();
    cout << "High performance laptop:" << endl;
    highPerformanceLaptop->describe();

    LaptopBuilder* lowPerformanceLaptopBuilder = new LowPerformanceLaptopBuilder();
    director->setLaptopBuilder(lowPerformanceLaptopBuilder);
    Laptop* lowPerformanceLaptop = director->getLaptop();
    cout << "Low performance laptop:" << endl;
    lowPerformanceLaptop->describe();
}

