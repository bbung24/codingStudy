#!/usr/bin/env python

'''
This file is for cracking the coding interview Chapter 10 : Sorting and Searching.
'''

from ..db import TNode, BinaryTree, LNode, LinkedList, DirectedTreeNode
import unittest
#------------------------------------------------------------------------------
def sorted_merge(a, b):
	"""
	10.1 Sorted Merge
	You are given two sorted arrays, A and B, where A has a large enough buffer
	at the end to hold B. Write a method to merge B into A in sorted order.
	"""
	if len(b) == 0:
		return a
	if len(a) == 0:
		return b
	indexA = 0
	indexB = 0
	while indexA < len(a) and indexB < len(b):
		if a[indexA] >= b[indexB]:
			put_value_array(a, indexA, b[indexB])
			indexB += 1
		else:
			indexA += 1
	if indexB != len(b):
		a += b[indexB:]
	return a

def put_value_array(a, index, value):
	a.insert(index, value)

#------------------------------------------------------------------------------
def group_anagrams(a):
	"""
	10.2 Group Anagrams
	Write a method to sort an array of strings so that all the anagrams are
	next to each other.
	"""
	pass

#------------------------------------------------------------------------------
def search_in_rotated_array(array):
	"""
	10.3 Search in Rotated Array
	Given a sorted array of n integers that has been rotated an unknown number
	of times, write code to find an element in the array. You may assume that
	the array was originally sorted in increasing order.
	"""
	pass

#------------------------------------------------------------------------------
def sorted_search_no_size(array):
	"""
	10.4 Sorted Search, No Size
	You are given an array-like data structure Listy which lacks a size method.
	It does, however, have an elementAt(i) method that returns the element at 
	index i in O(1) time. If i is beyond the bounds of the data structure, it 
	returns -1. (For this reason, the data structure only supports positive 
	integers.) Given a Listy which contains sorted, positive integers, find the
	index at which an element x occurs. If x occurs multiple times, you may return
	any index.
	"""
	pass

#------------------------------------------------------------------------------
def sorted_matrix_search(matrix):
	"""
	10.9 Sorted Matrix Search
	Given an M x N matrix in which each row and each column is sorted in
	ascedning order, write a method to find an element.
	"""
	
	pass

#------------------------------------------------------------------------------
# def rank_from_stream()

#------------------------------------------------------------------------------
class Test(unittest.TestCase):
	def test_sorted_merge(self):
		a = [1,5,7,23,46,78]
		b = [4,8,9,26,87,99]
		actual = sorted_merge(a,b)
		self.assertEqual([1,4,5,7,8,9,23,26,46,78,87,99], actual)

if __name__ == "__main__":
	unittest.main()