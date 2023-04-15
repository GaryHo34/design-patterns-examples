abstract class Tool {
    abstract describe(): string;
}

abstract class Axe extends Tool { }
abstract class Pickaxe extends Tool { }
abstract class Shovel extends Tool { }

class WoodAxe extends Axe {
    describe() {
        return "This is a wooden axe";
    }
}

class StoneAxe extends Axe {
    describe() {
        return "This is a stone axe";
    }
}

class IronAxe extends Axe {
    describe() {

        return "This is an iron axe";
    }
}

class WoodPickaxe extends Pickaxe {
    describe() {
        return "This is a wooden pickaxe";
    }
}

class StonePickaxe extends Pickaxe {
    describe() {
        return "This is a stone pickaxe";
    }
}

class IronPickaxe extends Pickaxe {
    describe() {
        return "This is an iron pickaxe";
    }
}

class WoodShovel extends Shovel {
    describe() {
        return "This is a wooden shovel";
    }
}

class StoneShovel extends Shovel {
    describe() {
        return "This is a stone shovel";
    }
}

class IronShovel extends Shovel {
    describe() {
        return "This is an iron shovel";
    }
}

abstract class ToolFactory {
    abstract createAxe(): Axe;
    abstract createPickaxe(): Pickaxe;
    abstract createShovel(): Shovel;
}


class WoodAxeFactory extends ToolFactory {
    createAxe(): Axe {
        return new WoodAxe();
    }
    createPickaxe(): Pickaxe {
        return new WoodPickaxe();
    }
    createShovel(): Shovel {
        return new WoodShovel();
    }
}

class StoneAxeFactory extends ToolFactory {
    createAxe(): Axe {
        return new StoneAxe();
    }
    createPickaxe(): Pickaxe {
        return new StonePickaxe();
    }
    createShovel(): Shovel {
        return new StoneShovel();
    }
}

class IronAxeFactory extends ToolFactory {
    createAxe(): Axe {
        return new IronAxe();
    }
    createPickaxe(): Pickaxe {
        return new IronPickaxe();
    }
    createShovel(): Shovel {
        return new IronShovel();
    }
}

class Client {
    private factory: ToolFactory;
    constructor(factory: ToolFactory) {
        this.factory = factory;
    }
    testToolFactory() {
        const axe = this.factory.createAxe();
        const pickaxe = this.factory.createPickaxe();
        const shovel = this.factory.createShovel();
        console.log(axe.describe());
        console.log(pickaxe.describe());
        console.log(shovel.describe(), '\n');
    }
}
let client: Client;

client = new Client(new WoodAxeFactory());
client.testToolFactory();

client = new Client(new StoneAxeFactory());
client.testToolFactory();

client = new Client(new IronAxeFactory());
client.testToolFactory();
