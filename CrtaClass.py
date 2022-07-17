from tkinter import N
import pygame
import math

SCALE = 10000


class Crta:
    def __init__(self, coordinate, angle, color, surfaceSize):
        self.coordinate = (int(coordinate[0]), int(coordinate[1]))
        self.angle = angle/360*2*math.pi
        self.color = color
        sineVal = math.sin(self.angle)
        cosineVal = math.cos(self.angle)
        screenX, screenY = surfaceSize

        scaleFactor = 1
        x, y = self.coordinate
        while(x > 1 and y > 100 and x < screenX-2 and y < screenY-2):
            scaleFactor += 1
            x = self.coordinate[0]-scaleFactor*cosineVal
            y = self.coordinate[1]-scaleFactor*sineVal

        self.c1 = (int(x), int(y))

        scaleFactor = 1
        x, y = self.coordinate
        while(x > 1 and y > 100 and x < screenX-2 and y < screenY-2):
            scaleFactor += 1
            x = self.coordinate[0]+scaleFactor*cosineVal
            y = self.coordinate[1]+scaleFactor*sineVal
        self.c2 = (int(x), int(y))

    def draw(self, surface):
        pygame.draw.line(surface, self.color, self.c1, self.c2)
        #pygame.draw.circle(surface, pygame.Color(0, 255, 0), self.c1, 4)
        #pygame.draw.circle(surface, pygame.Color(0, 0, 255), self.c2, 4)

    def findEdge(self, surface):
        k = 0
        if self.c2[0] != self.c1[0]:
            k = (self.c2[1]-self.c1[1])/(self.c2[0]-self.c1[0])

        n = self.c1[1]-k*self.c1[0]

        ranges = [(self.coordinate, self.c1), (self.coordinate, self.c2)]

        points = []
        for interval in ranges:
            prevPoint = interval[0]
            prevVal = surface.get_at(prevPoint)
            actualRange = range(interval[0][0], interval[1][0])
            if(interval[0][0] > interval[1][0]):
                actualRange = reversed(range(interval[1][0], interval[0][0]))
            for x in actualRange:
                newPoint = (x, int(k*x+n))
                val = surface.get_at(newPoint)
                if(val != prevVal):
                    prevVal = val
                    middle = ((prevPoint[0]+newPoint[0])/2,
                              (prevPoint[1]+newPoint[1])/2)
                    points.append(middle)
                    break
                prevPoint = newPoint
        return points
