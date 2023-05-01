public class Bridge {
    private interface Shape {
        void draw();
    }

    private class RedCircle implements Shape {
        private int x, y;
        private String color;

        public RedCircle(int x, int y) {
            this.x = x; 
            this.y = y; 
            this.color = "red";
        }

        public void draw() {
            System.out.println("Drawing a " + color + " circle at (" + x + ", " + y + ")");
        }
    }

    private class BlueSquare implements Shape {
        private int x, y;
        private String color;

        public BlueSquare(int x, int y) {
            this.x = x; 
            this.y = y; 
            this.color = "blue";
        }

        public void draw() {
            System.out.println("Drawing a " + color + " circle at (" + x + ", " + y + ")");
        }
    }

    private class Drawer {
        private Shape shape;

        public Drawer(Shape shape) {
            this.shape = shape;
        }

        public void draw() {
            shape.draw();
        }
    }

    public void testBridge() {
        Drawer drawer = new Drawer(new RedCircle(10, 10));
        drawer.draw();
        drawer = new Drawer(new BlueSquare(20, 20));
        drawer.draw();
    }


    public static void main(String[] args) {
        Bridge bridge = new Bridge();
        bridge.testBridge();
    }
}