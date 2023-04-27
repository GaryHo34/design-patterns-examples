import copy
import time


class DataSet:

    def __init__(self):
        print("Loading data from disk...")
        time.sleep(5)
        self.data = []
        self.id = 0

    def __str__(self):
        return str(self.data)


def testPrototype():
    d1 = DataSet()
    d2 = copy.copy(d1)
    d3 = copy.deepcopy(d1)

    d1.data.append(1)
    d2.data.append(2)
    d3.data.append(3)

    print("d1: " + str(d1))
    print("d2: " + str(d2))
    print("d3: " + str(d3))


if __name__ == "__main__":
    testPrototype()
