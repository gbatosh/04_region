class Shape:
    def area(self):
        print("the area of the figure: 0")
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        area = self.length ** 2
        print(f"the area of the square {area}")
shape = Shape()
shape.area()
square = Square(6)
square.area()
