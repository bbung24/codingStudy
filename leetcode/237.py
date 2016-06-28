#!/usr/bin/env python 
"""
237. Delete Node in a Linked List

Write a function to delete a node (except the tail) in a singly linked list, 
given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node 
with value 3, the linked list should become 1 -> 2 -> 4 after calling your 
function.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        if self.next:
            return str(self.val) + '->' + str(self.next)
        else:
            return str(self.val)

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next:
            next_val = node.next.val
            node.val = next_val
            node.next = node.next.next

import unittest 
class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_deleteNode(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        expected = ListNode(1)
        expected.next = ListNode(2)
        expected.next.next = ListNode(4)
        self.s.deleteNode(head.next.next)
        print head
        print expected