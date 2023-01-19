# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 11:53:48 2021

@author: afe02
"""

import shapes_begin as shapes

class ShapesContainer:
    def __init__(self):
        self._shapesList = []
    def append(self, shape):
        self._shapesList.append(shape)
    def __iter__(self):
        for s in self._shapesList:
            yield s
    def areas(self):
        # TODO implement a generator that generates areas for all
        for shape in self._shapesList:
            yield shape.area()


def main():
    shapesCont = ShapesContainer()
    shapesCont.append(shapes.Circle("c1", "green", 1))
    shapesCont.append(shapes.Circle("c2", "red", 2))
    shapesCont.append(shapes.Triangle("t1", "orange", 1, 2, 30))
    shapesCont.append(shapes.Triangle("t2", "yellow", 1, 2, 120))
    shapesCont.append(shapes.Triangle("t3", "black", 2, 2, 60))
    shapesCont.append(shapes.Rectangle("r1", "yellow", 1, 2))
    shapesCont.append(shapes.Rectangle("r2", "black", 5, 2))

    for s in shapesCont:
        s.printInfo()
    areaSum = 0
    for a in shapesCont.areas():
        areaSum += a

    print("Total area: " + str(areaSum))

if __name__ == '__main__':
    main()
