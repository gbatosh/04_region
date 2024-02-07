class Shape:
    def area(self):
        print("the area ofthe figure: 0")
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        area = self.length * self.width
        print(f"the area of the rectangle {area}")
area = Shape()
area.area()
rectangle = Rectangle(5, 3)
rectangle.area()  
