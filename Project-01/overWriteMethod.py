class Rectangle:
    def __init__(self):
        print('Inside into of Rectangle')
    def area(self, x, y):
        return x * y

class Square(Rectangle):
    def __init__(self):
        print ('Inside into of Square')
    def area(self, x):
        return Rectangle.area(self, x, x)

sq = Square()
print (sq.area(4))