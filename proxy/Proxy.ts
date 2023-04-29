interface Image {
    display(): void;
}

class RealImage implements Image {
    private fileName: string;
    constructor(fileName: string) {
        this.fileName = fileName;
        this.loadFromDisk(fileName);
    }
    display(): void {
        console.log('Displaying ' + this.fileName);
    }
    loadFromDisk(fileName: string): void {
        console.log('Loading ' + fileName);
    }
}

class ProxyImage implements Image {
    private realImage: RealImage;
    private fileName: string;
    constructor(fileName: string) {
        this.fileName = fileName;
    }
    display(): void {
        if (this.realImage === undefined) {
            this.realImage = new RealImage(this.fileName);
        }
        this.realImage.display();
    }
}

const image: Image = new ProxyImage('test_10mb.jpg');

// image will be loaded from disk
image.display();
console.log('');
// image will not be loaded from disk
image.display();
