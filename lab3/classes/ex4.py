import math 
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x,self.y)
    def move(self,x1,y1):
        self.x += x1
        self.y += y1
    def dist(self,x2,y2):
        x=self.x-x2
        y=self.y-y2
        g = math.sqrt(x**2+y**2)
        return g
p1=Point(1,2)
p1.move(3,4)
print(p1.dist(4,7))
p1.show()
