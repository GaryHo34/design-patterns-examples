from typing import Protocol


class Image(Protocol):
    def display_image(self):
        pass


class RealImage(Image):
    def __init__(self, filename):
        self._filename = filename
        self.load_image_from_disk()

    def load_image_from_disk(self):
        print("Loading   " + self._filename)


class ProxyImage(Image):
    def __init__(self, filename):
        self._filename = filename
        self._image = None

    def display_image(self):
        if self._image is None:
            self._image = RealImage(self._filename)
        self._image.display_image()


if __name__ == "__main__":

    proxy_image1 = ProxyImage("HiRes_10MB_Photo1")
    proxy_image2 = ProxyImage("HiRes_10MB_Photo2")

    proxy_image1.display_image()  # loading necessary
    proxy_image1.display_image()  # loading unnecessary
    proxy_image2.display_image()  # loading necessary
    proxy_image2.display_image()  # loading unnecessary
    proxy_image1.display_image()  # loading unnecessary
