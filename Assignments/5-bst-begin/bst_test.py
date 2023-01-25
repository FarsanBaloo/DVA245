# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 17:08:56 2021

@author: afe02
"""

import unittest
import binarysearchtree_begin as bst

class TestConstructBST(unittest.TestCase):
    def testConstructionNoArgIter(self):
        tree = bst.BinarySearchTree()
        self.assertIsNotNone(tree)
        i = 0
        for item in tree:
            i+= 1
        self.assertEqual(i, 0)
    def testConstructionRootIter(self):
        rootVal = 5
        root = bst.BinarySearchTree.Node(5)
        tree = bst.BinarySearchTree(root)
        self.assertIsNotNone(tree)
        i = 0
        for item in tree:
            i+= 1
            self.assertEqual(item, rootVal)
        self.assertEqual(i, 1)

class TestInsertIter(unittest.TestCase):
    def testInsertIter(self):
        items = [7, 3, 10]
        orderedItems = [3, 7, 10]
        tree = bst.BinarySearchTree()
        for i in items:
            tree.insert(i)
        ind = 0
        for i in tree:
            self.assertEqual(i, orderedItems[ind])
            ind += 1
        items = [1, 5, 8, 13]
        for i in items:
            tree.insert(i)
        orderedItems = [1, 3, 5, 7, 8, 10, 13]
        ind = 0
        for i in tree:
            self.assertEqual(i, orderedItems[ind])
            ind += 1
            
class TestMinMaxRemoveContains(unittest.TestCase):
    def setUp(self):
        self.t1 = bst.BinarySearchTree()
        self.t2 = bst.BinarySearchTree()
        self.t3 = bst.BinarySearchTree()
        items1 = [1, 3, 5, 7, 8, 10, 13]
        items2 = [13, 10, 8, 7, 5, 3, 1]
        items3 = [7, 3, 10, 1, 5, 8, 13]
        self.inTree = items1
        self.notInTree = [0, 2, 4, 6, 9, 11, 12, 14]
        for i in items1:
            self.t1.insert(i)
        for i in items2:
            self.t2.insert(i)
        for i in items3:
            self.t3.insert(i)
    def testMin(self):
        self.assertEqual(self.t1.min(), 1)
        self.assertEqual(self.t2.min(), 1)
        self.assertEqual(self.t3.min(), 1)
    def testMax(self):
        self.assertEqual(self.t1.max(), 13)
        self.assertEqual(self.t2.max(), 13)
        self.assertEqual(self.t3.max(), 13)
    def testRemove(self):
        # delete leaves
        self.t1.remove(13)
        items = [1, 3, 5, 7, 8, 10]
        ind = 0
        for i in self.t1:
            self.assertEqual(i, items[ind])
            ind+=1
        self.t2.remove(1)
        items = [3, 5, 7, 8, 10, 13]
        ind = 0
        for i in self.t2:
            self.assertEqual(i, items[ind])
            ind+=1
        # delete with one child
        self.t1.remove(1)
        items = [3, 5, 7, 8, 10]
        ind = 0
        for i in self.t1:
            self.assertEqual(i, items[ind])
            ind+=1
        self.t2.remove(5)
        self.t2.remove(13)
        items = [3, 7, 8, 10]
        ind = 0
        for i in self.t2:
            self.assertEqual(i, items[ind])
            ind+=1
        # delete with two children
        self.t3.remove(7)
        items = [1, 3, 5, 8, 10, 13]
        ind = 0
        for i in self.t3:
            self.assertEqual(i, items[ind])
            ind+=1
        self.t3.remove(3)
        self.t3.remove(10)
        items = [1, 5, 8, 13]
        ind = 0
        for i in self.t3:
            self.assertEqual(i, items[ind])
            ind+=1
    def testContains(self):
        for i in self.inTree:
            self.assertTrue(i in self.t1)
            self.assertTrue(i in self.t2)
            self.assertTrue(i in self.t3)
        for i in self.notInTree:
            self.assertFalse(i in self.t1)
            self.assertFalse(i in self.t2)
            self.assertFalse(i in self.t3)


if __name__ == '__main__':
    unittest.main()
