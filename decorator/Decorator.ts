interface IWeapon {
    describe(): void;
    getAttack(): number;
}

class Sword implements IWeapon {
    public describe(): void {
        console.log("This is a sword");
    }

    public getAttack(): number {
        return 20;
    }
}

interface IWeaponDecorator extends IWeapon { };

class SuperSwordDecorator implements IWeaponDecorator {
    private weapon: IWeapon;

    constructor(weapon: IWeapon) {
        this.weapon = weapon;
    }

    public describe(): void {
        console.log("This is a super sword");
        this.weapon.describe();
    }

    public getAttack(): number {
        return this.weapon.getAttack() + 10;
    }
}

function testDecorator() {
    const sword = new Sword();
    sword.describe();
    console.log("Attack: ", sword.getAttack());

    const superSword = new SuperSwordDecorator(sword);
    superSword.describe();
    console.log("Attack: ", superSword.getAttack());
}

testDecorator();