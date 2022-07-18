import math

class Point:
    def __init__(self, x, y):
        self.x = round(x)
        self.y = round(y)
    
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    
    def __add__(self, other):
        return Point(self.x+other.x,self.y+other.y)

    def __sub__(self, other):
        return Point(self.x-other.x,self.y-other.y)

    def get(self):
        return (self.x,self.y)             

    def __repr__(self):
        return "x: {}, y: {}".format(self.x,self.y)

    def __str__(self):
        return "Point x: {}, y: {}".format(self.x,self.y)

    def round(self):
        self.x = round(self.x)
        self.y = round(self.y)
        return self

    def distance(self):
        return math.sqrt(self.x**2+self.y**2)

    def distanceToPoint(self,other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)