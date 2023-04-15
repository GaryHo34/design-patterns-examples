
public class AbstractFactory {

    /* Axe Class */
    private abstract class Tool {
        public abstract String describe();
    }

    private abstract class Axe extends Tool {}

    private abstract class Pickaxe extends Tool {}

    private abstract class Shovel extends Tool {}

    // Wooden Axe
    private class WoodenAxe extends Axe {
        @Override
        public String describe() {
            return "This is a wooden axe";
        }
    }

    // Stone Axe
    private class StoneAxe extends Axe {
        @Override
        public String describe() {
            return "This is a stone axe";
        }
    }

    // Iron Axe
    private class IronAxe extends Axe {
        @Override
        public String describe() {
            return "This is an iron axe";
        }
    }

    // Wooden Pickaxe
    private class WoodenPickaxe extends Pickaxe {
        @Override
        public String describe() {
            return "This is a wooden pickaxe";
        }
    }

    // Stone Pickaxe
    private class StonePickaxe extends Pickaxe {
        @Override
        public String describe() {
            return "This is a stone pickaxe";
        }
    }

    // Iron Pickaxe
    private class IronPickaxe extends Pickaxe {
        @Override
        public String describe() {
            return "This is an iron pickaxe";
        }
    }

    // Wooden Shovel
    private class WoodenShovel extends Shovel {
        @Override
        public String describe() {
            return "This is a wooden shovel";
        }
    }

    // Stone Shovel
    private class StoneShovel extends Shovel {
        @Override
        public String describe() { 
            return "This is a stone shovel";
        }
    }

    // Iron Shovel
    private class IronShovel extends Shovel {
        @Override
        public String describe() {
            return "This is an iron shovel";
        }
    }

    /* Abstract factory*/
    public abstract class ToolFactory {
        public abstract Axe createAxe( );
        public abstract Pickaxe createPickaxe( );
        public abstract Shovel createShovel( );
    }

    public class WoodToolFactory extends ToolFactory {
        @Override
        public Axe createAxe( ) {
            return new WoodenAxe();
        }

        @Override
        public Pickaxe createPickaxe() {
            return new WoodenPickaxe();
        }

        @Override
        public Shovel createShovel() {
            return new WoodenShovel();
        }
    }

    public class StoneToolFactory extends ToolFactory {
        @Override
        public Axe createAxe() {
            return new StoneAxe();
        }

        @Override
        public Pickaxe createPickaxe() {
            return new StonePickaxe();
        }

        @Override
        public Shovel createShovel() {
            return new StoneShovel();
        }
    }

    public class IronToolFactory extends ToolFactory {
        @Override
        public Axe createAxe() {
            return new IronAxe();
        }

        @Override
        public Pickaxe createPickaxe() {
            return new IronPickaxe();
        }

        @Override
        public Shovel createShovel() {
            return new IronShovel();
        }
    }

    private class Client {
        private ToolFactory factory;
        public Client(ToolFactory factory) {
            this.factory = factory;
        }
        public void testToolFactory() {
            var axe = factory.createAxe();
            var pickaxe = factory.createPickaxe();
            var shovel = factory.createShovel();

            System.out.println(axe.describe());
            System.out.println(pickaxe.describe());
            System.out.println(shovel.describe());
            System.out.println();
        }
    }

    public void test() {
        var client = new Client(new WoodToolFactory());
        client.testToolFactory();

        client = new Client(new StoneToolFactory());
        client.testToolFactory();

        client = new Client(new IronToolFactory());
        client.testToolFactory();
    }


    public static void main(String[] args) {
        AbstractFactory testToolFactory = new AbstractFactory();
        testToolFactory.test();
        return;
    }
}