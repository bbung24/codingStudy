#!/usr/bin/env python
"""
113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:

Given the below binary tree and sum = 22
          5
      4      8
   11     13   4
  7  2        5 1

return
[
    [5,4,11,2],
    [5,8,4,5]
]
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.sum = sum
        self.result = []
        if root:
            self.helper(root, 0, [])
        return self.result

    def helper(self, node, sum_now, path):
        sum_now += node.val
        path.append(node.val)
        if not node.left and not node.right:
            if sum_now == self.sum:
                self.result.append([x for x in path])
        elif abs(sum_now) < abs(self.sum):
            if node.left:
                self.helper(node.left, sum_now, path)
            if node.right:
                self.helper(node.right, sum_now, path)
        sum_now -= node.val
        path.pop()
        
import unittest
class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_pathSum(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        left = root.left
        left.left = TreeNode(11)
        left.left.left = TreeNode(7)
        left.left.right = TreeNode(2)
        right = root.right
        right.left = TreeNode(13)
        right.right = TreeNode(4)
        right.right.left = TreeNode(5)
        right.right.right = TreeNode(1)
        expected = [
            [5,4,11,2],
            [5,8,4,5]
        ]
        actual = self.s.pathSum(root, 22)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()