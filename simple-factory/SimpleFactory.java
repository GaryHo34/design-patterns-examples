
public class SimpleFactory {

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
    public class CraftingFactory {

        public Axe createAxe(Material material) {
            Axe axe;
            switch (material) {
                case WOOD:
                    axe = new WoodenAxe();
                    break;
                case STONE:
                    axe = new StoneAxe();
                    break;
                case IRON:
                    axe = new IronAxe();
                    break;
                default:
                    throw new IllegalArgumentException("Invalid material");
            }
            return axe;
        }
    }

    public void testCraftingFactory() {
        CraftingFactory  craftinTable = new CraftingFactory();
        
        var woodAxe = craftinTable.createAxe(Material.WOOD);
        var stoneAxe = craftinTable.createAxe(Material.STONE);
        var ironAxe = craftinTable.createAxe(Material.IRON);

        System.out.println("WoodAxe is made of " + woodAxe.getMaterial());
        System.out.println("StoneAxe is made of " + stoneAxe.getMaterial());
        System.out.println("IronAxe is made of " + ironAxe.getMaterial());
    }

    public static void main(String[] args) {
        SimpleFactory simpleFactory = new SimpleFactory();
        simpleFactory.testCraftingFactory();
    }
}