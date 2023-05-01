class Shape:
    def draw(self):
        raise NotImplementedError


class RedCircle(Shape):
    x: int
    y: int
    color: str

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = "red"

    def draw(self):
        print(f"Drawing a {self.color} circle at ({self.x}, {self.y})")


class BlueSquare(Shape):
    x: int
    y: int
    color: str

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = "blue"

    def draw(self):
        print(f"Drawing a {self.color} square at ({self.x}, {self.y})")


class Drawer:
    shape: Shape

    def __init__(self, shape: Shape):
        self.shape = shape

    def draw(self):
        self.shape.draw()


def test_bridge():
    drawer = Drawer(RedCircle(10, 10))
    drawer.draw()
    drawer = Drawer(BlueSquare(20, 20))
    drawer.draw()


if __name__ == "__main__":
    test_bridge()