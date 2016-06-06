#!/usr/bin/env python

'''
This file is for cracking the coding interview Chapter 4 : Trees and Graphs.
'''

class Node(object):
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value

class BinaryTree(object):
	def __init__(self):
		self.root = None

#------------------------------------------------------------------------------
def checkBinary(tree):
	'''
	4.1
	Implement a function to check if a binary tree is balanced. For the purposes of
	this question, a balanced tree is defined to be a tree such that the heights of the
	two subtrees of any node never differ by more than one.
	'''
	def getHeight(tree):
		if tree.left != None:
			left_height = getHeight(tree.left)
		else:
			left_height = 0
		if tree.right != None:
			right_height = getHeight(tree.right)
		else:
			right_height = 0
		if abs(left_height - right_height) > 1:
			raise Exception('Not Binary')
		sub_height = max(left_height, right_height)
		return sub_height + 1
	# What if tree is null ? What should I return ?
	if tree == None:
		return False # return false because it is not a tree at all
	try:
		getHeight(tree)
	except Exception:
		return False
	return True

#------------------------------------------------------------------------------
class DirectedTree(object):
	def __init__(self, value):
		self.value = value
		self.neighbors = []

	def __str__(self):
		return 'DirectedTree('+str(self.value)+'):'+str(self.neighbors)

	def __repr__(self):
		return self.__str__()

#------------------------------------------------------------------------------
def existsRoute(a, b):
	'''
	4.2
	Given a directed graph, design an algorithm to find out whether there is a route
	between two nodes.
	'''
	from Queue import Queue
	check_list = Queue()
	checked = set()
	for n in a.neighbors:
		if n == b:
			return True
		if n not in checked:
			check_list.put((n,b))
			checked.add(n)
	for n in b.neighbors:
		if n == a:
			return True
		if n not in checked:
			check_list.put((n,a))
			checked.add(n)
	print check_list.empty()
	while not check_list.empty():
		node, target = check_list.get()
		print check_list
		print checked
		print node
		for n in node.neighbors:
			print n
			if n == target:
				return True
			if n not in checked:
				check_list.put((n, target))
				checked.add(n)
	return False

def testSet():
	one = DirectedTree(1)
	two = DirectedTree(2)
	three = DirectedTree(3)
	four = DirectedTree(4)
	five = DirectedTree(5)
	six = DirectedTree(6)
	seven = DirectedTree(7)
	eight = DirectedTree(8)
	two.neighbors.append(one)
	one.neighbors.append(three)
	one.neighbors.append(four)
	one.neighbors.append(five)
	six.neighbors.append(one)
	six.neighbors.append(seven)
	seven.neighbors.append(five)
	eight.neighbors.append(seven)
	return existsRoute(two, seven)



#------------------------------------------------------------------------------
# 6th edition.
def min_tree(array):
	"""
	4.2 Minimal Tree
	Given a sorted (increasing order) array with unique integer elements, write
	an algorithm to create a binary search tree with minimal height.
	"""
	graph = BinaryTree()
	graph.root = min_tree_helper(array, 0, len(array)-1)
	return graph

def min_tree_helper(array, left, right):
	if left > right:
		return
	mid_index = (left + right) / 2
	mid_val = array[mid_index]
	node = Node(mid_val)
	node.left = min_tree_helper(array, left, mid_index-1)
	node.right = min_tree_helper(array, mid_index+1, right)
	return node

import unittest
class Test(unittest.TestCase):
	def test_min_tree(self):
		array = [1, 2, 3, 4, 5]
		graph = BinaryTree()
		graph.root = Node(3)
		n = graph.root
		n.left = Node(1)
		n.right = Node(4)
		n.left.right = Node(2)
		n.right.right = Node(5)
		actual = min_tree(array)
		self.assertEqual(self.check_graph(actual.root, graph.root), True)

		array = [1, 2, 3, 4, 5, 6, 7, 8]
		graph = BinaryTree()
		graph.root = Node(4)
		n = graph.root
		n.left = Node(2)
		n.right = Node(6)
		n.left.left = Node(1)
		n.left.right = Node(3)
		n.right.left = Node(5)
		n.right.right = Node(7)
		n.right.right.right = Node(8)
		actual = min_tree(array)
		self.assertEqual(self.check_graph(actual.root, graph.root), True)

	def check_graph(self, g1, g2):
		if g1 == None and g2 == None:
			return True
		elif g1 == None or g2 == None:
			return False
		if g1.value == g2.value:
			return self.check_graph(g1.left, g2.left) and self.check_graph(g1.right, g2.right)
		else:
			return False

if __name__ == "__main__":
	unittest.main()
