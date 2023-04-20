public class Decorator {
    private interface IWeapon {
        void describe();

        int getAttack();
    }

    private class Sword implements IWeapon {

        @Override
        public void describe() {
            System.out.println("This is a sword");
        }

        @Override
        public int getAttack() {
            return 10;
        }
    }

    private interface IWeaponDecorator extends IWeapon {

    }

    private class SuperSwordDecarator implements IWeaponDecorator {

        protected IWeapon weapon;

        public SuperSwordDecarator(IWeapon weapon) {
            this.weapon = weapon;
        }

        @Override
        public void describe() {
            System.out.println("This is an upgraded");
            weapon.describe();
        }

        @Override
        public int getAttack() {
            return weapon.getAttack() + 5;
        }
    }

    public void testDecorator() {
        Sword sword = new Sword();
        // normal sword
        sword.describe();
        System.out.println("Attack: " + sword.getAttack() + "\n");

        // super sword
        SuperSwordDecarator superSword = new SuperSwordDecarator(sword);
        superSword.describe();
        System.out.println("Attack: " + superSword.getAttack());
    }

    public static void main(String[] args) {
        Decorator decorator = new Decorator();
        decorator.testDecorator();
    }
}