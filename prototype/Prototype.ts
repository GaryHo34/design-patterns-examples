class DataSet {
    private id: number;
    data: number[];

    constructor() {
        this.data = [];
        this.id = 1;
    }

    async setup() {
        console.log("Loading data from disk...");
        await new Promise(resolve => setTimeout(resolve, 1000));
        this.data = [...this.data, 1, 2, 3];
    }

    clone() {
        const clone = Object.create(this);
        clone.data = [...this.data];
        clone.id = this.id;
        return clone;
    }
}

const testPrototype = async () => {
    // Wait 5 sec to construct an object
    const d1: DataSet = new DataSet();

    // Typescrit won't allow the waiting for construction
    // We simulate an expensive data setup process
    await d1.setup();

    // Clone the object (vid clone method)
    // No need to setup the data again
    const d2 = d1.clone();

    // Test the deep copy
    d1.data = [...d1.data, 1];
    d2.data = [...d2.data, 2];

    console.log("d1: " + d1.data.join(", "));
    console.log("d2: " + d2.data.join(", "));
}

testPrototype();