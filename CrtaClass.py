from tkinter import N
import pygame
import math

SCALE = 10000


class Crta:
    def __init__(self, coordinate, angle, color, surfaceSize):
        self.coordinate = coordinate
        self.angle = angle/360*2*math.pi
        self.color = color
        sineVal = math.sin(self.angle)
        cosineVal = math.cos(self.angle)
        screenX, screenY = surfaceSize

        scaleFactor = 1
        x, y = coordinate
        while(x > 1 and y > 1 and x < screenX-2 and y < screenY-2):
            scaleFactor += 1
            x = coordinate[0]-scaleFactor*cosineVal
            y = coordinate[1]-scaleFactor*sineVal

        self.c1 = (int(x), int(y))

        scaleFactor = 1
        x, y = coordinate
        while(x > 1 and y > 1 and x < screenX-2 and y < screenY-2):
            scaleFactor += 1
            x = coordinate[0]+scaleFactor*cosineVal
            y = coordinate[1]+scaleFactor*sineVal
        self.c2 = (int(x), int(y))

    def draw(self, surface):
        pygame.draw.line(surface, self.color, self.c1, self.c2)
        pygame.draw.circle(surface, pygame.Color(0, 255, 0), self.c1, 4)
        pygame.draw.circle(surface, pygame.Color(0, 0, 255), self.c2, 4)

    def findEdge(self, surface):
        k = 0
        if self.c2[0] != self.c1[0]:
            k = (self.c2[1]-self.c1[1])/(self.c2[0]-self.c1[0])

        n = self.c1[1]-k*self.c1[0]

        prevVal = surface.get_at(self.c1)
        points = []
        ranges = (self.c1[0], self.c2[0])
        if(self.c1[0] > self.c2[0]):
            ranges = (self.c2[0], self.c1[0])
        for x in range(*ranges):
            y = int(k*x+n)
            val = surface.get_at((x, y))
            if(val != prevVal):
                prevVal = val
                points.append((x, y))
        return points
