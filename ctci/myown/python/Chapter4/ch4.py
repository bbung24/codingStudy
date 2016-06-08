#!/usr/bin/env python

'''
This file is for cracking the coding interview Chapter 4 : Trees and Graphs.
'''

from ..db import TNode, BinaryTree, LNode, LinkedList
# class Node(object):
# 	def __init__(self, value):
# 		self.left = None
# 		self.right = None
# 		self.value = value

# class BinaryTree(object):
# 	def __init__(self):
# 		self.root = None

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
	while not check_list.empty():
		node, target = check_list.get()
		for n in node.neighbors:
			if n == target:
				return True
			if n not in checked:
				check_list.put((n, target))
				checked.add(n)
	return False

def existsRouteSet():
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
	node = TNode(mid_val)
	node.left = min_tree_helper(array, left, mid_index-1)
	node.right = min_tree_helper(array, mid_index+1, right)
	return node

#------------------------------------------------------------------------------
def list_of_depths(tree):
	"""
	4.3 List of Depths
	Given a binary tree, design an algorithm which creates a linked list of all
	the nodes at each depth (e.g., if you have a tree with depth D, you'll have
	D linked lists).
	"""
	if tree.root == None:
		return []
	result = []
	currentDepth = []
	nextDepth = []
	node = tree.root
	ll = LinkedList()
	while node != None:
		ll.addNode(node.value)
		if node.left != None:
			nextDepth.append(node.left)
		if node.right != None:
			nextDepth.append(node.right)
		if len(currentDepth) == 0 and len(nextDepth) != 0:
			currentDepth = nextDepth
			nextDepth = []
			node = currentDepth.pop()
			result.append(ll)
			ll = LinkedList()
		elif len(currentDepth) != 0:
			node = currentDepth.pop()
		else:
			break
	result.append(ll)
	return result

#------------------------------------------------------------------------------
def is_balanced(tree):
	"""
	4.4 Check Balanced
	Implement a function to check if a binary tree is balanced. For the purposes
	of this question, a balanced tree is defined to be a tree such that the heights
	of the two subtrees of any node never differ by more than one.
	"""
	if tree.root == None:
		return False
	try:
		is_balanced_helper(tree.root)
	except:
		return False
	else:
		return True

def is_balanced_helper(node):
	if node == None:
		return 0
	left = is_balanced_helper(node.left)
	right = is_balanced_helper(node.right)
	if abs(left - right) > 1:
		raise Exception('Not Balanced Tree')
	else:
		return max(left, right) + 1

#------------------------------------------------------------------------------
def validate_bst(tree):
	"""
	4.5 Validate BST
	Implement a function to check if a binary tree is a binary search tree.
	"""
	if tree.root == None:
		return True
	try:
		validate_helper(tree.root)
	except:
		return False
	else:
		return True

def validate_helper(node):
	max_val = node.value
	min_val = node.value
	if node.left:
		(left_max, left_min) = validate_helper(node.left)
		if left_max > node.value:
			raise Exception("Not BST")
		else:
			min_val = left_min
	if node.right:
		(right_max, right_min) = validate_helper(node.right)
		if right_min < node.value:
			raise Exception("Not BST")
		else:
			max_val = right_max
	return max_val, min_val

import unittest
class Test(unittest.TestCase):
	def test_min_tree(self):
		array = [1, 2, 3, 4, 5]
		graph = BinaryTree()
		graph.root = TNode(3)
		n = graph.root
		n.left = TNode(1)
		n.right = TNode(4)
		n.left.right = TNode(2)
		n.right.right = TNode(5)
		actual = min_tree(array)
		self.assertEqual(self.check_graph(actual.root, graph.root), True)

	def test_min_tree2(self):
		array = [1, 2, 3, 4, 5, 6, 7, 8]
		graph = BinaryTree()
		graph.root = TNode(4)
		n = graph.root
		n.left = TNode(2)
		n.right = TNode(6)
		n.left.left = TNode(1)
		n.left.right = TNode(3)
		n.right.left = TNode(5)
		n.right.right = TNode(7)
		n.right.right.right = TNode(8)
		actual = min_tree(array)
		self.assertEqual(self.check_graph(actual.root, graph.root), True)

	def test_list_of_depths(self):
		graph = BinaryTree()
		graph.root = TNode(4)
		n = graph.root
		n.left = TNode(2)
		n.right = TNode(6)
		n.left.left = TNode(1)
		n.left.right = TNode(3)
		n.right.left = TNode(5)
		n.right.right = TNode(7)
		n.right.right.right = TNode(8)
		actual = list_of_depths(graph)
		# for l in actual:
		# 	print l
		pass # Good

	def check_graph(self, g1, g2):
		if g1 == None and g2 == None:
			return True
		elif g1 == None or g2 == None:
			return False
		if g1.value == g2.value:
			return self.check_graph(g1.left, g2.left) and self.check_graph(g1.right, g2.right)
		else:
			return False

	def test_is_balanced(self):
		tree = BinaryTree()
		tree.root = TNode(1)
		n = tree.root
		n.left = TNode(2)
		n.right = TNode(3)
		actual = is_balanced(tree)
		self.assertEqual(True, actual)

	def test_is_balanced2(self):
		tree = BinaryTree()
		tree.root = TNode(1)
		n = tree.root
		n.left = TNode(2)
		n.right = TNode(3)
		n.left.left = TNode(4)
		n.left.right = TNode(5)
		actual = is_balanced(tree)
		self.assertEqual(True, actual)

	def test_is_balanced3(self):
		tree = BinaryTree()
		tree.root = TNode(1)
		n = tree.root
		n.left = TNode(2)
		n.right = TNode(3)
		n.left.left = TNode(4)
		n.left.left.left = TNode(5)
		actual = is_balanced(tree)
		self.assertEqual(False, actual)

	def test_validate_bst(self):
		tree = BinaryTree()
		tree.root = TNode(3)
		n = tree.root
		n.left = TNode(1)
		n.right = TNode(3)
		n.left.right = TNode(4)
		actual = validate_bst(tree)
		self.assertEqual(False, actual)

	def test_validate_bst2(self):
		tree = BinaryTree()
		tree.root = TNode(3)
		n = tree.root
		n.left = TNode(1)
		n.right = TNode(3)
		n.left.right = TNode(2)
		actual = validate_bst(tree)
		self.assertEqual(True, actual)	

	def test_validate_bst3(self):
		tree = BinaryTree()
		tree.root = TNode(4)
		n = tree.root
		n.left = TNode(3)
		n.left.left = TNode(2)
		n.left.left.left = TNode(1)
		actual = validate_bst(tree)
		self.assertEqual(True, actual)

	def test_validate_bst4(self):
		tree = BinaryTree()
		tree.root = TNode(1)
		n = tree.root
		n.right = TNode(2)
		n.right.right = TNode(3)
		n.right.right.right = TNode(4)
		actual = validate_bst(tree)
		self.assertEqual(True, actual)

	def test_validate_bst5(self):
		tree = BinaryTree()
		tree.root = TNode(2)
		n = tree.root
		n.right = TNode(4)
		n.right.left = TNode(1)
		actual = validate_bst(tree)
		self.assertEqual(False, actual)

	def test_validate_bst6(self):
		tree = BinaryTree()
		tree.root = TNode(2)
		n = tree.root
		n.right = TNode(4)
		n.right.left = TNode(3)
		actual = validate_bst(tree)
		self.assertEqual(True, actual)


if __name__ == "__main__":
	unittest.main()
