#!/usr/bin/env python

'''
This file is for cracking the coding interview Chapter 4 : Trees and Graphs.
'''

from ..db import TNode, BinaryTree, LNode, LinkedList, DirectedTreeNode
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
	one = DirectedTreeNode(1)
	two = DirectedTreeNode(2)
	three = DirectedTreeNode(3)
	four = DirectedTreeNode(4)
	five = DirectedTreeNode(5)
	six = DirectedTreeNode(6)
	seven = DirectedTreeNode(7)
	eight = DirectedTreeNode(8)
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

#------------------------------------------------------------------------------
def successor(node):
	"""
	4.6 Successor
	Write an algorithm to find the "next" node (i.e., in-order successor) of
	a given node in a binary search tree. You may assume that each node has a link
	to its parent.
	"""
	if node.right:
		return recursive_down(node.right)
	return recursive_up(node)

def recursive_down(node):
	if node.left:
		return recursive_down(node.left)
	else:
		return node

def recursive_up(node):
	if node.parent:
		if node.parent.right == node:
			return recursive_up(node.parent)
		else:
			return node.parent
	else:
		return None

#------------------------------------------------------------------------------
def build_order(projects, dependencies):
	"""
	4.7 Build Order
	You are given a list of projects and a list of dependencies (which is a list of
	pairs of projects, where the second project is dependent on the first project).
	All of project's dependencies must be built before the project is. Find a build
	order that will allow the projects to be built. If there is no valid build order,
	return an error.
	"""
	if len(projects) == 0:
		raise Exception('Impossible')
	graph = {}
	queue = []
	dep = [x for x in dependencies]
	for value in projects:
		node = DirectedTreeNode(value)
		node.visited = False
		graph[value] = node
		queue.append(node)
	for value_from, value_to in dependencies:
		node_to = graph[value_to]
		node_from = graph[value_from]
		node_from.neighbors.append(node_to)
		try:
			queue.pop(queue.index(node_to))
		except:
			pass
	result = []
	while len(queue) != 0:
		node = queue.pop(0)
		if node.visited:
			raise Exception('Cycle')
		node.visited = True
		result.append(node.value)
		for n in node.neighbors:
			if not n in queue:
				queue.append(n)
	if len(result) != len(projects):
		raise Exception('Cycle')
	return result

#------------------------------------------------------------------------------
def common_ancestor(n1, n2):
	"""
	4.8 First Common Ancestor
	Design an algorithm and write code to find the first common ancestor
	of two nodes in a binary tree. Avoid storing additional nodes in a data
	structure. NOTE: This is not necessarily a binary search tree.
	"""
	mark_parents(n1)
	return mark_parents(n2)

def mark_parents(node):
	if node == None:
		return None
	if hasattr(node, 'visited') and node.visited == True:
		return node
	else:
		node.visited = True
		return mark_parents(node.parent)

#------------------------------------------------------------------------------
from itertools import permutations
def bst_sequences(tree):
	"""
	4.9 BST Sequences
	A binary search tree was created by traversing through an array from left to
	right and inserting each element. Given a binary search tree with distict
	elements, print all possible arrays that could have led to this tree.
	"""
	if tree.root == None:
		return
	depth_nodes = build_depth_nodes(tree)
	result = []
	print_recursive(depth_nodes, 0, '{', result)
	return result
	
def print_recursive(dn, depth, string, result):
	if not depth in dn:
		result.append(string[:-1] + '}')
	else:
		for p in permutations(dn[depth]):
			next = string
			for n in p:
				next += str(n.value) + ','
			print_recursive(dn, depth+1, next, result)

def build_depth_nodes(tree):
	queue = []
	depth = 0
	depth_nodes = {}
	next_depth_node = tree.root
	queue.append(tree.root)
	while len(queue) != 0:
		node = queue.pop(0)
		if node.left:
			queue.append(node.left)
		if node.right:
			queue.append(node.right)
		if not depth in depth_nodes:
			depth_nodes[depth] = []
		depth_nodes[depth].append(node)
		if node == next_depth_node and len(queue) > 0:
			depth += 1
			next_depth_node = queue[-1]
	return depth_nodes


#------------------------------------------------------------------------------
import unittest
class Test(unittest.TestCase):
	def test_bst_sequence(self):
		graph = BinaryTree()
		graph.root = TNode(4)
		n = graph.root
		n.left = TNode(2)
		n.right = TNode(6)
		n.left.left = TNode(1)
		n.left.right = TNode(3)
		n.right.left = TNode(5)
		n.right.right = TNode(7)
		bst_sequences(graph)

	def initialize_common_ancestor(self):
		n1 = TNode(1)
		n2 = TNode(2)
		n3 = TNode(3)
		n4 = TNode(4)
		n5 = TNode(5)
		n6 = TNode(6)
		n7 = TNode(7)
		n8 = TNode(8)
		n1.left = n2
		n2.parent = n1
		n1.right = n3
		n3.parent = n1
		n2.left = n4
		n4.parent = n2
		n2.right = n5
		n5.parent = n2
		n3.left = n6
		n6.parent = n3
		n3.right = n7
		n7.parent = n3
		return n1, n2, n3, n4, n5, n6, n7, n8

	def test_common_ancestor(self):
		n1, n2, n3, n4, n5, n6, n7, n8 = self.initialize_common_ancestor()
		actual = common_ancestor(n4, n7)
		self.assertEqual(n1, actual)
		n1, n2, n3, n4, n5, n6, n7, n8 = self.initialize_common_ancestor()
		actual = common_ancestor(n4, n5)
		self.assertEqual(n2, actual)
		n1, n2, n3, n4, n5, n6, n7, n8 = self.initialize_common_ancestor()
		actual = common_ancestor(n6, n7)
		self.assertEqual(n3, actual)
		n1, n2, n3, n4, n5, n6, n7, n8 = self.initialize_common_ancestor()
		actual = common_ancestor(n3, n7)
		self.assertEqual(n3, actual)
		n1, n2, n3, n4, n5, n6, n7, n8 = self.initialize_common_ancestor()	
		actual = common_ancestor(n4, n8)
		self.assertEqual(None, actual)

	def test_build_order(self):
		projects = ['a','b','c','d','e','f']
		dependencies = [('a','d'), ('f','b'), ('b','d'), ('f','a'), ('d','c')]
		actual = build_order(projects, dependencies)
		self.assertEqual(['e','f','b','a','d','c'], actual)

	def test_build_order2(self):
		projects = ['a','b','c','d','e','f']
		dependencies = [('a','d'), ('d','b'), ('b','f'), ('f','a'), ('d','c')]
		with self.assertRaises(Exception):
			actual = build_order(projects, dependencies)

	def test_successor(self):
		n1 = TNode(1)
		n2 = TNode(2)
		n3 = TNode(3)
		tree = BinaryTree()
		tree.root = n2
		n2.left = n1
		n1.parent = n2
		n2.right = n3
		n3.parent = n2
		actual = successor(n1)
		self.assertEqual(n2, actual)
		actual = successor(n2)
		self.assertEqual(n3, actual)
		actual = successor(n3)
		self.assertEqual(None, actual)

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
