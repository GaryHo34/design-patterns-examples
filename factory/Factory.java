
public class Factory {

    /* Axe Class */
    private interface Axe {
        String getMaterial();
    }

    private enum Material {
        WOOD,
        STONE,
        IRON
    }

    // Wooden Axe
    private class WoodenAxe implements Axe {
        @Override
        public String getMaterial() {
            return "wood";
        }
    }

    // Stone Axe
    private class StoneAxe implements Axe {
        @Override
        public String getMaterial() {
            return "stone";
        }
    }

    // Iron Axe
    private class IronAxe implements Axe {
        @Override
        public String getMaterial() {
            return "iron";
        }
    }

    /* Simple factory*/
    public abstract class AxeFactory {

        public abstract Axe createAxe(Material material);
    }

    public class WoodAxeFactory extends AxeFactory {
        @Override
        public Axe createAxe(Material material) {
            if(material != Material.WOOD)
                throw new IllegalArgumentException("Invalid material");
            return new WoodenAxe();
        }
    }

    public class StoneAxeFactory extends AxeFactory {
        @Override
        public Axe createAxe(Material material) {
            if(material != Material.STONE)
                throw new IllegalArgumentException("Invalid material");
            return new StoneAxe();
        }
    }

    public class IronAxeFactory extends AxeFactory {
        @Override
        public Axe createAxe(Material material) {
            if(material != Material.IRON)
                throw new IllegalArgumentException("Invalid material");
            return new IronAxe();
        }
    }

    public void testAxeFactory() {
        AxeFactory factory;

        factory = new WoodAxeFactory();
        var woodAxe = factory.createAxe(Material.WOOD);

        factory = new StoneAxeFactory();
        var stoneAxe = factory.createAxe(Material.STONE);

        factory = new IronAxeFactory();
        var ironAxe = factory.createAxe(Material.IRON);

        System.out.println("WoodAxe is made of " + woodAxe.getMaterial());
        System.out.println("StoneAxe is made of " + stoneAxe.getMaterial());
        System.out.println("IronAxe is made of " + ironAxe.getMaterial());
    }

    public static void main(String[] args) {
        Factory testFactory = new Factory();
        testFactory.testAxeFactory();
    }
}