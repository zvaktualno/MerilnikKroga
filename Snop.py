from calendar import c
from cmath import inf
from re import I
import pygame
import math
import skg

from CrtaClass import Crta
from Point import Point


class Snop:
    def __init__(self, coordinate, color, numberOfLines, surfaceSize):
        self.coordinate = coordinate
        self.color = color
        self.surfaceSize = surfaceSize
        self.setNumberOfLines(numberOfLines)
        self.circle = None
        self.maxCircle = None
        self.minCircle = None

    def setNumberOfLines(self, n):

        self.lines = []
        self.collisionPoints = []
        for lineNum in range(n):
            self.lines.append(
                Crta(Point(*self.coordinate), int(180/n*lineNum), self.color, self.surfaceSize))


    def draw(self, surface):
        #for line in self.lines:
        #    line.draw(surface)
        #for point in self.collisionPoints:
        #    pygame.draw.circle(surface, pygame.Color(0, 255, 0), point.get(), 5)
        if self.circle is not None and self.maxCircle is not None and self.minCircle is not None:
            pygame.draw.circle(surface, pygame.Color(
                0, 0, 255), self.circle[1].get(), self.circle[0], width=2)
            '''pygame.draw.circle(surface, pygame.Color(
                0, 255, 255), self.maxCircle[1], self.maxCircle[0], width=2)
            pygame.draw.circle(surface, pygame.Color(
                0, 255, 0), self.minCircle[1], self.minCircle[0], width=2)'''
    def reset(self):
        self.collisionPoints =[]
        self.circle = None
        self.maxCircle = None
        self.minCircle = None

    def find(self, surface):
        self.reset()
        collisionPoints = []
        collisionPointsVals = []
        for line in self.lines:
            linePoints = line.findEdge(surface)
            if linePoints is None:
                return False
            for point in linePoints:
                collisionPoints.append(point)
                collisionPointsVals.append(point.get())

        self.collisionPoints = collisionPoints
        circle = skg.nsphere_fit(collisionPointsVals)
        r = circle[0]
        center = Point(*circle[1])
        self.circle = (r,center)

        furthestPoint = center
        closestPoint = Point(1000,1000)

        for point in self.collisionPoints:
            distance = point.distanceToPoint(center)
            if(distance > furthestPoint.distance()):
                furthestPoint = point
            if(distance < closestPoint.distance()):
                closestPoint = point

        self.maxCircle = (furthestPoint.distance(), furthestPoint)
        self.minCircle = (closestPoint.distance(), closestPoint)
        return True
