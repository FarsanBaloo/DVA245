# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 13:25:04 2021

@author: afe02
"""
import unittest
import shapes_begin as shapes
import shapes_container_begin as shapes_container
import math


        
class TestShapesContainer(unittest.TestCase):
    def testAppendIterAreas(self):
        s1 = shapes_container.shapes.Circle("c2", "blue", 2)
        s2 = shapes.Triangle("taa1", "red", 2, 2, 60)
        s3 = shapes.Rectangle("r2", "white", 3.5, 2)
        shapesList = shapes_container.ShapesContainer()
        shapesList.append(s1)
        shapesList.append(s2)
        shapesList.append(s3)
        it = iter(shapesList)
        sFirst = next(it)
        self.assertEqual(sFirst.name(), "c2")
        sSecond = next(it)
        self.assertEqual(sSecond.color(), "red")
        sThird = next(it)
        self.assertEqual(sThird.circumference(), 11)
        sumArea = 0;
        aIt = iter(shapesList.areas())
        a1 = next(aIt)
        self.assertAlmostEqual(a1, 4 * math.pi)
        a2 = next(aIt)
        self.assertAlmostEqual(a2, math.sqrt(3))
        a3 = next(aIt)
        self.assertAlmostEqual(a3, 7)
        
        
if __name__ == '__main__':
    unittest.main()
    