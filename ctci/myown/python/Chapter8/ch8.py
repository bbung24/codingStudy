#!/usr/bin/env python

'''
This file is for cracking the coding interview Chapter 8 : Recursive and Dynamic Programming
'''

import unittest 

#------------------------------------------------------------------------------
def triple_step(n):
	'''
	8.1 Triple Step
	A child is running up a staircase with n steps and can hop either 1 step, 
	2 steps, or 3 steps at a time. Implement a method to count how many possible
	ways the child can run up the stairs.
	'''
	cache = {1:1, 2:2, 3:4}
	return triple_step_helper(n, cache)

def triple_step_helper(n, cache):
	if n in cache:
		return cache[n]
	else:
		result = (triple_step_helper(n-1, cache) + triple_step_helper(n-2, cache) +
			triple_step_helper(n-3, cache))
		cache[n] = result
		return result

class TestClass(unittest.TestCase):
	def test_triple_step1(self):
		actual = triple_step(6)
		self.assertEqual(24, actual)

	def test_triple_step2(self):
		actual = triple_step(5)
		self.assertEqual(13, actual)

if __name__ == "__main__":
	unittest.main()