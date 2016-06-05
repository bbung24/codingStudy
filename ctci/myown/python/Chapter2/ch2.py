#!/usr/bin/env python

'''
This file is for cracking the coding interview Chapter 2 : Linked List.
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self,value):
        node = Node(value)
        #if the old list is none, set new node as the first node
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def __str__(self):
        if self.head != None:
            index = self.head
            nodestore = [str(index.value)]
            while index.next != None:
                index = index.next
                nodestore.append(str(index.value))
            return "LinkedList  [ " + "->".join(nodestore) + " ]"
        return "LinkedList  []"

    def __repr__(self):
        return self.__str__()

    #remove the first node that have the same value as the given node_value
    def removeNode(self, node_value):
        current = self.head
        if current.value == node_value:
            self.head = self.head.next
        while(current.next != None):
            if current.next.value == node_value:
                current.next = current.next.next
                break
            else:
                current = current.next

# #------------------------------------------------------------------------------
# class Node(object):
#     '''
#     Singly linked list
#     '''
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

#     def __str__(self):
#         output = 'LinkedList: ('
#         node = self
#         if node == None:
#             output += ')'
#             return output
#         while node.next != None:
#             output += str(node.value) + '->'
#             node = node.next
#         output += str(node.value) + ')'
#         return output

#     def __repr__(self):
#         return self.__str__()

#     def appendToTail(self, value):
#         node = Node(value, None)
#         if self.next == None:
#             self.next = node
#         else:
#             tail = self
#             while tail.next != None:
#                 tail = tail.next
#             tail.next = node

def deleteNode(head, d):
    '''
    Delete a node from given linked list
    '''
    if head.value == d:
        return head.next
    cur = head
    while cur.next != None:
        if cur.next.value == d:
            cur.next = cur.next.next
            return head
        cur = cur.next
    return head

#------------------------------------------------------------------------------
def deleteDup(ll):
	'''
	2.1
	Write code to remove duplicates from an unsorted linked list.
	'''
	if ll.head != None:
		values = set()
		prev = None
		cur = ll.head
		while cur.next != None:
			if cur.value in values:
				prev.next = cur.next
			else:
				values.add(cur.value)
				prev = cur
			cur = cur.next
		if cur.value in values:
			prev.next = cur.next

def deleteDup2(ll):
	'''
	2.1
	FOLLOW UP
	How would you solve this problem if a temporary buffer is not allowed?
	'''
	if ll.head != None:
		cur = ll.head
		while cur.next != None:
			checker = cur.next
			prev = cur
			while checker.next != None:
				if checker.value == cur.value:
					prev.next = checker.next
				else:
					prev = checker
				checker = checker.next
			if checker.value == cur.value:
				prev.next = checker.next
			cur = cur.next

#------------------------------------------------------------------------------
def kthFromLast(ll, k):
	'''
	2.2
	Implement an algorithm to find the kth to last element of a singly 
	linked list.
	'''
	if ll == None:
		raise BaseException("LinkedList is null")
	if ll.head == None:
		raise BaseException("LinkedList's head is null")
	pt = ll.head
	for i in range(0, k-1):
		if pt.next == None:
			raise BaseException("LinkedList doesn't have enough elements")
		pt = pt.next
	pt2 = ll.head
	while pt.next != None:
		pt = pt.next
		pt2 = pt2.next
	return pt2

#------------------------------------------------------------------------------
def deleteMiddleNode(node):
	'''
	2.3
	Implement an algorithm to delete a node in the middle of a singly linked 
	list, given only access to that node.
	EXAMPLE
	Input: the node c from the linked list a->b->c->d->e
	Result: nothing is returned, but the new linked list looks like a->b->d->e
	'''
	if node == None: 
		raise BaseException('Given node is null')
	if node.next == None:
		node = None
	while node.next.next != None:
		node.value = node.next.value
		node = node.next
	node.value = node.next.value
	node.next = None

#------------------------------------------------------------------------------
def partitionll(ll, x):
	'''
	2.4
	Write code to partition a linked list around a value x, such that all nodes
	less than x come before all nodes greater than or equal to x.
	'''
	if ll == None:
		raise BaseException("LinkedList is null")
	if ll.head == None:
		raise BaseException("LinkedList is empty")
	head = ll.head
	left = right = first_left = first_right = None
	while head.next != None:
		if head.value < x:
			if left == None:
				left = Node(head.value)
				first_left = left
			else:
				left.next = Node(head.value)
				left = left.nextl
		elif head.value >= x:
			if right == None:
				right = Node(head.value)
				first_right = right
			else:
				right.next = Node(head.value)
				right = right.next
		head = head.next
	if head.value < x:
		if left == None:
			left = Node(head.value)
		else:
			left.next = Node(head.value)
			left = left.next
	elif head.value >= x:
		if right == None:
			right = Node(head.value)
		else:
			right.next = Node(head.value)
			right = right.next
	if left == None:
		left = first_right
	else:
		left.next = first_right
	return first_left

#------------------------------------------------------------------------------
def sumDigits(one, two):
	'''
	2.5
	You have two numbers represented by a linked list, where each node contains
	a single digit. The digits are stored in reverse order, such that the Ts
	digit is at the head of the list. Write a function that adds the two numbers
	and returns the sum as a linked list.
	EXAMPLE
	Input:(7-> 1 -> 6) + (5 -> 9 -> 2). That is : 617 + 295.
	Output: 2 -> 1 -> 9.That is, 912.
	'''
	if (one == None or one.head == None) and (two == None or two.head == None):
		raise BaseException("Both numbers are none.")
	carry = False
	output = None
	result = None
	first = None
	second = None
	if one != None:
		first = one.head
	if two != None:
		second = two.head
	while first != None and second != None:
		temp = first.value + second.value
		if carry == True:
			temp += 1
		if temp >= 10:
			num = temp - 10
			carry = True
		else:
			num = temp
			carry = False
		node = Node(num)
		if result == None:
			output = LinkedList()
			output.head = node
			result = output.head
		else:
			result.next = node
			result = result.next
		first = first.next
		second = second.next
	rest = None
	if first == None:
		rest = second
	elif second == None:
		rest = first
	while rest != None:
		num = rest.value
		if carry == True:
			num += 1
			carry = False
		node = Node(num)
		if result == None and output == None:
			output = LinkedList()
			output.head = node
			result = output.head
		elif result == None:
			result = node
		else:
			result.next = node
			result = result.next
		rest = rest.next
	if carry == True:
		node = Node(1)
		result.next = node
	return output


def sumDigits2(one, two):
	'''
	2.5-2
	FOLLOW UP
	Suppose the digits are stored in forward order. Repeat the above problem. 
	EXAMPLE
	Input:(6 -> 1 -> 7) + (2 -> 9 -> 5). That is : 617 + 295.
	Output: 9 -> 1 -> 2. That is, 912.
	'''
	new_one = new_two = None
	if one != None and one.head != None:
		new_one = reverseLL(one)
	if two != None and two.head != None:
		new_two = reverseLL(two)
	return reverseLL(sumDigits(new_one, new_two))

def reverseLL(ll):
	'''
	reverse linked list
	'''
	new = LinkedList()
	new_head = None
	node = ll.head
	while node.next != None:
		temp = new_head
		new_head = Node(node.value)
		new_head.next = temp
		node = node.next
	temp = new_head
	new_head = Node(node.value)
	new_head.next = temp
	new.head = new_head
	return new

#------------------------------------------------------------------------------
def findCircularHead(ll):
	'''
	2.6
	Given a circular linked list, implement an algorithm which returns the node
	at the beginning of the loop.
	
	DEFINITION
	Circular linked list: A (corrupt) linked list in which a node's next pointer 
	points to an earlier node, so as to make a loop in the linked list.
	
	EXAMPLE
		Input:A ->B->C->D->E-> C[the same C as earlier] 
		Output:C
	'''
	if ll == None or ll.head == None:
		raise BaseException("LinkedList is none.")
	exist = set()
	node = ll.head
	while node.next != None:
		if node in exist:
			return node
		else:
			exist.add(node)
		node = node.next
	if node in exist:
		return node
	raise BaseException("LinkedList is not circular linked list.")
#------------------------------------------------------------------------------
def isPalindrome(ll):
	'''
	2.7
	Implement a function to check if a linked list is a palindrome.

	palindrome ? sequence of list is same in backward or forward order.
	'''
	reverse = reverseLL(ll)
	node1 = ll.head
	node2 = reverse.head
	while node1.next != None:
		if node1.value != node2.value:
			return False
		node1 = node1.next
		node2 = node2.next
	return True

#------------------------------------------------------------------------------
# 6th edition
def intersect(ll1, ll2):
	"""
	2.7 Intersection
	Given two (singly) linked lists, determine if the two lists intersect. Return
	the intersecting node. Note that the intersection is defined based on reference,
	not value. That is, if the kth node of the first linked list is the exact same
	node (by reference) as the jth node of the second linked list, then they are
	intersecting.
	"""
	if ll1 == None or ll2 == None:
		return None
	check = {}
	node = ll1
	while node != None:
		if node in check:
			break
		check[node] = 0
		node = node.next
	node = ll2
	while node != None:
		if node in check:
			return node
		node = node.next
	return None

import unittest
class Test(unittest.TestCase):
    '''Test Cases'''
    def test_intersect(self):
    	n1 = Node(1)
    	n2 = Node(2)
    	n3 = Node(3)
    	n4 = Node(1)
    	n5 = Node(2)

    	ll1 = None
    	n1.next = n2
    	n2.next = n3
    	ll2 = n1
    	actual = intersect(ll1, ll2)
    	self.assertEqual(actual, None)

    	n4.next = n5
    	ll1 = n4
    	actual = intersect(ll1, ll2)
    	self.assertEqual(actual, None)

    	n5.next = n1
    	actual = intersect(ll1, ll2)
    	self.assertEqual(actual, n1)
        
if __name__ == "__main__":
    unittest.main()






























