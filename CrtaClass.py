import pygame
import math
from Point import Point

class Crta:
    def __init__(self, coordinate, angle, color, surfaceSize):
        self.coordinate = coordinate
        self.angle = angle/360*2*math.pi
        self.color = color
        sineVal = math.sin(self.angle)
        cosineVal = math.cos(self.angle)
        screenX, screenY = surfaceSize

        #find one end
        scaleFactor = 1
        self.c1 = coordinate
        while(self.c1.x > 0 and self.c1.y > 100 and self.c1.x < screenX and self.c1.y < screenY):
            scaleFactor+=1
            self.c1 = coordinate - Point(scaleFactor*cosineVal,scaleFactor*sineVal)
        scaleFactor-=1
        self.c1 = coordinate - Point(scaleFactor*cosineVal,scaleFactor*sineVal)

        #find the other end
        scaleFactor = 1
        self.c2 = coordinate
        while(self.c2.x > 0 and self.c2.y > 100 and self.c2.x < screenX and self.c2.y < screenY):
            scaleFactor+=1
            self.c2 = coordinate + Point(scaleFactor*cosineVal,scaleFactor*sineVal)
        scaleFactor-=1
        self.c2 = coordinate + Point(scaleFactor*cosineVal,scaleFactor*sineVal)

    def draw(self, surface):
        pygame.draw.line(surface, self.color, self.c1.get(), self.c2.get())
        #pygame.draw.circle(surface, pygame.Color(0, 255, 0), self.c1.get(), 4)
        #pygame.draw.circle(surface, pygame.Color(0, 0, 255), self.c2.get(), 4)

    def findEdge(self, surface):
        k = math.inf
        diff = self.c2-self.c1
        if diff.x != 0:
            k = diff.y/diff.x

        n = self.c1.y-k*self.c1.x
        insideOutRange = [(self.coordinate, self.c1), (self.coordinate, self.c2)]
        outsideInRange = [(self.c1, self.coordinate), (self.c2, self.coordinate)]
        ranges = insideOutRange

        points = []
        for interval in ranges:
            prevPoint = interval[0]

            #get value at point
            print(prevPoint)
            prevVal = surface.get_at(prevPoint.get())

            #search by x or y
            XsearchParams = (interval[0].x, interval[1].x)
            YsearchParams = (interval[0].y, interval[1].y)

            searchParams = XsearchParams
            if k>1 or k<-1:
                searchParams = YsearchParams

            actualRange = range(*searchParams)

            if(searchParams[0] > searchParams[1]):
                actualRange = reversed(range(searchParams[1],searchParams[0]))

            for x in actualRange:
                newPoint = None
                if k>1 or k<-1:
                    if k == math.inf:
                        newPoint = Point(interval[0].x, x)
                    else:
                        newPoint = Point((x-n)/k, x)
                else:                
                    newPoint = Point(x, k*x+n)

                val = surface.get_at(newPoint.get())
                if(val != prevVal):
                    prevVal = val
                    middle = Point((prevPoint.x + newPoint.x)/2,
                              (prevPoint.y + newPoint.y)/2)
                    points.append(newPoint)
                    break
                prevPoint = newPoint
        if(len(points)<2):
            return None
        return points

    def __str__(self):
        return "Middle point: {}, Start Point: {}, End Point:{}".format(str(self.coordinate),str(self.c1),str(self.c2))
