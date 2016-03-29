"""
2. Add Two Numbers

You are given two linked lists representing two non-negative numbers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self): 
        return str(self.val)

def display_node(lst):
    if lst:
        if lst.next:
            print("{} -> ".format(lst)),
            display_node(lst.next)
        else:
            print "{}".format(lst)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        olim = 0
        head = pointer = None
        while l1 or l2:
            value = olim
            if l1:
                value += l1.val
            if l2:
                value += l2.val
            if value >= 10:
                olim = 1
                value -= 10
            else:
                olim = 0
            if head == None:
                head = ListNode(value)
                pointer = head
            else:
                pointer.next = ListNode(value)
                pointer = pointer.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if olim > 0:
            pointer.next = ListNode(1)
        return head

if __name__ == "__main__":
    test = Solution()
    l1 = ListNode(2)
    # l1.next = ListNode(4)
    # l1.next.next = ListNode(3)
    display_node(l1)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(9)
    display_node(l2)
    display_node(test.addTwoNumbers(l1, l2))