class geometry:
    def __init__(self, x, y):
        self.side = x
        self.radius = y
    def square(self):
        return self.side * self.side
    def sqrPerimeter(self):
        return self.side * 4

    def cirPerimeter(self):
        return 2 * 3.1416 * self.radius
    def diameter(self):
        return 2 * self.radius

class myClass:
    def add(self):
        add = self.A + self.B
        return add