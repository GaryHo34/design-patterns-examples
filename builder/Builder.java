public class Builder {
    private class Laptop {
        String cpu;
        String ram;
        String os;

        public Laptop() {
            this.cpu = "";
            this.ram = "";
            this.os = "";
        }

        public void setCpu(String cpu) {
            this.cpu = cpu;
        }

        public void setRam(String ram) {
            this.ram = ram;
        }

        public void setOs(String os) {
            this.os = os;
        }

        public void describe() {
            System.out.println("CPU: " + cpu);
            System.out.println("RAM: " + ram);
            System.out.println("OS: " + os);
        }
    }

    private abstract class LaptopBuilder {
        public abstract void setCpu();

        public abstract void setRam();

        public abstract void setOs();

        public abstract Laptop build();
    }

    private class HighPerformanceLaptopBuilder extends LaptopBuilder {
        private Laptop highPerformanceLaptop;

        public HighPerformanceLaptopBuilder() {
            highPerformanceLaptop = new Laptop();
        }

        @Override
        public void setCpu() {
            highPerformanceLaptop.setCpu("i7 CPU");
        }

        @Override
        public void setRam() {
            highPerformanceLaptop.setRam("16GB RAM");
        }

        @Override
        public void setOs() {
            highPerformanceLaptop.setOs("Windows 10");
        }

        @Override
        public Laptop build() {
            return highPerformanceLaptop;
        }
    }

    private class LowPerformanceLaptopBuilder extends LaptopBuilder {
        private Laptop lowPerformanceLaptop;

        public LowPerformanceLaptopBuilder() {
            lowPerformanceLaptop = new Laptop();
        }

        @Override
        public void setCpu() {
            lowPerformanceLaptop.setCpu("i3 CPU");
        }

        @Override
        public void setRam() {
            lowPerformanceLaptop.setRam("4GB RAM");
        }

        @Override
        public void setOs() {
            lowPerformanceLaptop.setOs("Windows 7");
        }

        @Override
        public Laptop build() {
            return lowPerformanceLaptop;
        }
    }

    private class Director {
        private LaptopBuilder laptopBuilder = null;

        public void setLaptopBuilder(LaptopBuilder laptopBuilder) {
            this.laptopBuilder = laptopBuilder;
        }

        public Laptop getLaptop() {
            laptopBuilder.setCpu();
            laptopBuilder.setRam();
            laptopBuilder.setOs();
            return laptopBuilder.build();
        }
    }

    public void testLaptopBuilder() {
        Director director = new Director();
        LaptopBuilder highPerformanceLaptopBuilder = new HighPerformanceLaptopBuilder();
        director.setLaptopBuilder(highPerformanceLaptopBuilder);
        Laptop highPerformanceLaptop = director.getLaptop();
        System.out.println("High performance laptop:");
        highPerformanceLaptop.describe();

        LaptopBuilder lowPerformanceLaptopBuilder = new LowPerformanceLaptopBuilder();
        director.setLaptopBuilder(lowPerformanceLaptopBuilder);
        Laptop lowPerformanceLaptop = director.getLaptop();
        System.out.println("Low performance laptop:");
        lowPerformanceLaptop.describe();
    }

    public static void main(String[] args) {
        Builder builder = new Builder();
        builder.testLaptopBuilder();
    }
}