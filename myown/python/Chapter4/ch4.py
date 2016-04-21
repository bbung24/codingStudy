#!/usr/bin/env python

'''
This file is for cracking the coding interview Chapter 4 : Trees and Graphs.
'''

class BinaryTree(object):
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value

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
	














