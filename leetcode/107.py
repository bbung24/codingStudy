#!/usr/bin/env python
"""
107. Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes'
values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7]

return its bottom-up level order traversal as:
[
    [15,7],
    [9,20],
    [3]
]
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return 'TreeNode({})'.format(self.val)
    def __repr__(self):
        return self.__str__()

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        current_queue = [root]
        next_queue = []
        current_level = []
        while len(current_queue) != 0 or len(next_queue) != 0:
            current = current_queue.pop(0)
            current_level.append(current.val)
            if current.left:
                next_queue.append(current.left)
            if current.right:
                next_queue.append(current.right)
            if len(current_queue) == 0:
                current_queue = next_queue
                next_queue = []
                result.append(current_level)
                current_level = []
        result.reverse()
        return result

import unittest
class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_levelOrderBottom(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        right = root.right
        right.left = TreeNode(15)
        right.right = TreeNode(7)
        expected = [[15,7],[9,20],[3]]
        actual = self.s.levelOrderBottom(root)
        self.assertEqual(actual, expected)