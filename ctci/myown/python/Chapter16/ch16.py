#!/usr/bin/env python

'''
This file is for cracking the coding interview Chapter 16 : Moderate
'''

import unittest
#------------------------------------------------------------------------------
def num_swap(a, b):
	'''
	16.1 Number Swapper
	Write a function to swap a number in place (that is, without temporary variables).
	'''
	if a > b:
		a += b
		b = a - b
		a = a - b
	else:
		b += a
		a = b - a
		b = b - a
	return a, b

def num_swap_sol(a, b):
	"""
	Solution from the book uses xor operator
	"""
	a = a ^ b
	b = a ^ b
	a = a ^ b
	return a, b

#------------------------------------------------------------------------------
class TestClass(unittest.TestCase):
	def test_num_swap(self):
		actual = num_swap(6, 4)
		self.assertEqual((4, 6), actual)

	def test_num_swap_sol(self):
		actual = num_swap_sol(6, 4)
		self.assertEqual((4, 6), actual)

if __name__ == '__main__':
	unittest.main()