from cmath import inf
import pygame
import math
import skg

from CrtaClass import Crta


class Snop:
    def __init__(self, coordinate, color, numberOfLines, surfaceSize):
        self.coordinate = coordinate
        self.color = color
        numberOfLines = int(numberOfLines/2)
        self.lines = []
        self.collisionPoints = []
        for lineNum in range(numberOfLines):
            self.lines.append(
                Crta(coordinate, 360/numberOfLines*lineNum, color, surfaceSize))
        self.circle = None
        self.maxCircle = None
        self.minCircle = None

    def draw(self, surface):
        # for line in self.lines:
        #    line.draw(surface)
        for point in self.collisionPoints:
            pygame.draw.circle(surface, pygame.Color(255, 0, 0), point, 5)
        if self.circle is not None and self.maxCircle is not None and self.minCircle is not None:
            pygame.draw.circle(surface, pygame.Color(
                0, 0, 255), self.circle[1], self.circle[0], width=2)
            '''pygame.draw.circle(surface, pygame.Color(
                0, 255, 255), self.maxCircle[1], self.maxCircle[0], width=2)
            pygame.draw.circle(surface, pygame.Color(
                0, 255, 0), self.minCircle[1], self.minCircle[0], width=2)'''

    def find(self, surface):
        for line in self.lines:
            for point in line.findEdge(surface):
                self.collisionPoints.append(point)

        self.circle = skg.nsphere_fit(self.collisionPoints)
        x, y = self.circle[1]

        furthestPoint = 0
        closestPoint = inf

        for point in self.collisionPoints:
            distance = math.sqrt((point[0]-x)**2+(point[1]-y)**2)
            if(distance > furthestPoint):
                furthestPoint = distance
            if(distance < closestPoint):
                closestPoint = distance
        self.maxCircle = (furthestPoint, (x, y))
        self.minCircle = (closestPoint, (x, y))
