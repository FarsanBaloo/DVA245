# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 13:25:04 2021

@author: afe02
"""
import unittest
import shapes_begin as shapes
import math



class TestCircle(unittest.TestCase):
    def setUp(self):
        self._circle1 = shapes.Circle("c1", "red", 1)
        self._circle2 = shapes.Circle("c2", "blue", 2)
    def testNameColor(self):
        self.assertEqual(self._circle1.name(), "c1")
        self.assertEqual(self._circle2.name(), "c2")
        self.assertEqual(self._circle1.color(), "red")
        self.assertEqual(self._circle2.color(), "blue")
    def testArea(self):
        area1 = math.pi
        area2 = 4 * math.pi
        self.assertAlmostEqual(self._circle1.area(), area1)
        self.assertAlmostEqual(self._circle2.area(), area2)
    def testCircumference(self):
        circ1 = 2* math.pi
        circ2 = 4 * math.pi
        self.assertAlmostEqual(self._circle1.circumference(), circ1)
        self.assertAlmostEqual(self._circle2.circumference(), circ2)
        
        
class TestTriangle(unittest.TestCase):
    def setUp(self):
        self._triangleAcuteAngle1 = shapes.Triangle("taa1", "red", 2, 2, 60)
        self._triangleAcuteAngle2 = shapes.Triangle("taa2", "black", math.sqrt(3), 2, 30)
        self._triangleAcuteAngle3 = shapes.Triangle("taa3", "red", 1, math.sqrt(2), 45)
        self._triangleObtuseAngle1 = shapes.Triangle("toa1", "red", 1, 2, 120) 
    def testNameColor(self):
        self.assertEqual(self._triangleAcuteAngle1.name(), "taa1")
        self.assertEqual(self._triangleAcuteAngle2.name(), "taa2")
        self.assertEqual(self._triangleAcuteAngle1.color(), "red")
        self.assertEqual(self._triangleAcuteAngle2.color(), "black")
    def testArea(self):
        areaAA1  = math.sqrt(3)
        areaAA2 = areaAA1/2
        areaAA3 = 0.5
        areaOA1 = areaAA2
        self.assertAlmostEqual(self._triangleAcuteAngle1.area(), areaAA1)
        self.assertAlmostEqual(self._triangleAcuteAngle2.area(), areaAA2)
        self.assertAlmostEqual(self._triangleAcuteAngle3.area(), areaAA3)
        self.assertAlmostEqual(self._triangleObtuseAngle1.area(), areaOA1)
    def testCircumference(self):
        circAA1 = 6
        circAA2 = 3 + math.sqrt(3)
        circAA3 = 2 + math.sqrt(2)
        circOA1 = 3 + math.sqrt(7)
        self.assertAlmostEqual(self._triangleAcuteAngle1.circumference(), circAA1)
        self.assertAlmostEqual(self._triangleAcuteAngle2.circumference(), circAA2)
        self.assertAlmostEqual(self._triangleAcuteAngle3.circumference(), circAA3)
        self.assertAlmostEqual(self._triangleObtuseAngle1.circumference(), circOA1)
        
class TestRectangle(unittest.TestCase):
    def setUp(self):
        self._rect1 = shapes.Rectangle("r1", "red", 2, 4)
        self._rect2 = shapes.Rectangle("r2", "white", 3.5, 2)
    def testNameColor(self):
        self.assertEqual(self._rect1.name(), "r1")
        self.assertEqual(self._rect2.name(), "r2")
        self.assertEqual(self._rect1.color(), "red")
        self.assertEqual(self._rect2.color(), "white")
    def testArea(self):
        area1 = 8
        area2 = 7
        self.assertAlmostEqual(self._rect1.area(), area1)
        self.assertAlmostEqual(self._rect2.area(), area2)
    def testCircumference(self):
        circ1 = 12
        circ2 = 11
        self.assertAlmostEqual(self._rect1.circumference(), circ1)
        self.assertAlmostEqual(self._rect2.circumference(), circ2)
        
        
if __name__ == '__main__':
    unittest.main()
    