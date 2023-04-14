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

abstract class AxeFactory {
    abstract createAxe(material: Material): Axe;
}

class WoodAxeFactory extends AxeFactory {
    createAxe(material: Material): Axe {
        if(material !== Material.WOOD)
            throw new Error("WoodAxeFactory can only create WoodAxe");
        return new WoodAxe();
    }
}

class StoneAxeFactory extends AxeFactory {
    createAxe(material: Material): Axe {
        if(material !== Material.STONE)
            throw new Error("StoneAxeFactory can only create StoneAxe");
        return new StoneAxe();
    }
}

class IronAxeFactory extends AxeFactory {
    createAxe(material: Material): Axe {
        if(material !== Material.IRON)
            throw new Error("IronAxeFactory can only create IronAxe");
        return new IronAxe();
    }
}

const testAxeFactory = () => {
    
    let factory : AxeFactory;

    factory = new WoodAxeFactory();
    const woodAxe = factory.createAxe(Material.WOOD);

    factory = new StoneAxeFactory();
    const stoneAxe = factory.createAxe(Material.STONE);

    factory = new IronAxeFactory();
    const ironAxe = factory.createAxe(Material.IRON);

    console.log("WoodAxe is made of",woodAxe.getMaterial());
    console.log("StoneAxe is made of",stoneAxe.getMaterial());
    console.log("IronAxe is made of",ironAxe.getMaterial());
}

testAxeFactory();