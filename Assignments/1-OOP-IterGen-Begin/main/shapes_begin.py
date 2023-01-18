# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 11:53:48 2021

@author: afe02
@ revised RiSo 18-Jan 2023
"""

import math
class Shape:
    """"Shape is an abstract base class used for the concrete implementations"""
    def __init__(self, name, color):
        self._name = name
        self._color = color
        
    def name(self):
        return self._name
    def color(self):
        return self._color
    def area(self):
        raise NotImplementedError("The area function is not defined for the "
                                  "abstract shape")    
    def circumference(self):
        raise NotImplementedError("The circumference function is not defined "
                                  "for the abstract shape")
    def printInfo(self):
        print("Shape "  + self.name() + " is a " + self.color() + " " + 
              type(self).__name__ + f" with area {self.area():.2f}" 
              + f" and circumference {self.circumference():.2f}" )
        
class Circle(Shape):
    """The Circle class implements a circle with a given radius"""
    def __init__(self, name, color, radius):
        super().__init__(name, color)
        self._radius = radius
    def area(self):
        return math.pi * math.pow(self._radius, 2)
    def circumference(self):
        return 2 * math.pi * self._radius
    
    
class Triangle(Shape):
    """"The Triangle class implements a triangle determined by the length of
    two sides and the angle between them given in degrees. Angle must be > 0 and < 180"""
    def __init__(self, name, color, side1, side2, angle12):
        super().__init__(name, color)
        self._side1 = side1
        self._side2 = side2
        # angle in radians
        angle12Rad = angle12*2*math.pi/360
        self._base = side1
        self._height = side2*math.sin(angle12Rad)
        self._side3 = \
            math.sqrt(math.pow(self._base - side2*math.cos(angle12Rad), 2) + \
                      math.pow(self._height,2))
        return

    def area(self):
        return self._base * self._height/2
    def circumference(self):
        return self._side1 + self._side2 + self._side3
    
class Rectangle(Shape):
    """The Rectangle class implements a rectangle with a given base and height"""
    def __init__(self, name, color, base, height):
        # TODO implement the Rectangle constructor
        super().__init__(name, color)
        self._base = base
        self._height = height
        return

    def area(self):
        # TODO implement the Rectangle area method
        return self._base*self._height
    def circumference(self):
        # TODO implement the Rectangle circumference method
        return 2*(self._base+self._height)
    

