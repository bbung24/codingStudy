#!/usr/bin/env python
"""
98. Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than
        the node's key.
    The right subtree of a node contains only nodes with keys greater than
        the node's key.
    Both the left and right subtrees must also be binary search trees.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        if root.left:
            try:
                mini, maxi = self.getMiniMaxi(root.left)
            except:
                return False
            if maxi >= root.val:
                return False
        if root.right:
            try:
                mini, maxi = self.getMiniMaxi(root.right)
            except: 
                return False
            if mini <= root.val:
                return False
        return True
        
    def getMiniMaxi(self, root):
        minimum = root.val
        maximum = root.val
        if root.left:
            mini, maxi = self.getMiniMaxi(root.left)
            minimum = min(minimum, mini)
            maximum = max(maximum, maxi)
            if maxi >= root.val:
                raise
        if root.right:
            mini, maxi = self.getMiniMaxi(root.right)
            minimum = min(minimum, mini)
            maximum = max(maximum, maxi)
            if mini <= root.val:
                raise
        return minimum, maximum

import unittest
class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_isValidBST(self):
        head = TreeNode(2)
        left = TreeNode(1)
        head.left = left
        right = TreeNode(3)
        head.right = right
        expected = True
        actual = self.s.isValidBST(head)
        self.assertEqual(actual, expected)

    def test_isValidBST2(self):
        head = TreeNode(1)
        left = TreeNode(2)
        head.left = left
        right = TreeNode(3)
        head.right = right
        expected = False
        actual = self.s.isValidBST(head)
        self.assertEqual(actual, expected)