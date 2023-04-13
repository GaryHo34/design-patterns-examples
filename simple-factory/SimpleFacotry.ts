interface Axe {
    getMaterial(): string;
}

enum Material {
    WOOD,
    STONE,
    IRON
}

class WoodAxe implements Axe {
    getMaterial() {
        return "wood";
    }
}

class StoneAxe implements Axe {
    getMaterial() {
        return "stone";
    }
}

class IronAxe implements Axe {
    getMaterial() {
        return "iron";
    }
}

class CraftingFactory {
    static createAxe(material: Material): Axe {
        switch (material) {
            case Material.WOOD:
                return new WoodAxe();
            case Material.STONE:
                return new StoneAxe();
            case Material.IRON:
                return new IronAxe();
        }
    }
}

const testCraftingFactory = () => {
    const woodAxe = CraftingFactory.createAxe(Material.WOOD);
    const stoneAxe = CraftingFactory.createAxe(Material.STONE);
    const ironAxe = CraftingFactory.createAxe(Material.IRON);
    console.log("WoodAxe is made of ",woodAxe.getMaterial());
    console.log("StoneAxe is made of ",stoneAxe.getMaterial());
    console.log("IronAxe is made of ",ironAxe.getMaterial());
}

testCraftingFactory();