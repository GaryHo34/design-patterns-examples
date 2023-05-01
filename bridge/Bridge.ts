interface Shape {
    draw(): void;
}

class RedCircle implements Shape {
    private x: number;
    private y: number;
    private color: string;

    constructor(x: number, y: number) {
        this.x = x;
        this.y = y;
        this.color = "red";
    }

    public draw(): void {
        console.log(`Drawing a ${this.color} circle at (${this.x}, ${this.y})`);
    }
}

class BlueSquare implements Shape {

    private x: number;
    private y: number;
    private color: string;

    constructor(x: number, y: number) {
        this.x = x;
        this.y = y;
        this.color = "blue";
    }

    public draw(): void {
        console.log(`Drawing a ${this.color} circle at (${this.x}, ${this.y})`);
    }
}

class Drawer {
    private shape: Shape;

    constructor(shape: Shape) {
        this.shape = shape;
    }

    public draw(): void {
        this.shape.draw();
    }
}

const testBridge = () => {
    let drawer: Drawer = new Drawer(new RedCircle(10, 10));
    drawer.draw();
    drawer = new Drawer(new BlueSquare(20, 20));
    drawer.draw();
}

testBridge();