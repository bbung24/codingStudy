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

#------------------------------------------------------------------------------
def robot_in_a_grid(grid):
	"""
	8.2 Robot in a Grid
	Imagine a robot sitting on the upper left corner of grid with r rows and c 
	columns. The robot can only move in two directions, right and down, but 
	certain cells are "off limits" such that the robot cannot step on them.
	Design an algorithm to find a path for the robot from the top left to the 
	bottom right.
	"""
	result = []
	robot_helper(grid, result, 0, 0)
	return result

def robot_helper(grid, result, row, col):
	result.append((row,col))
	if row == len(grid)-1 and col == len(grid[0])-1:
		return True
	if grid[row][col] == 1:
		result.pop()
		return False
	elif col+1 < len(grid[0]) and robot_helper(grid, result, row, col+1):
		return True
	elif row+1 < len(grid) and robot_helper(grid, result, row+1, col):
		return True
	else:
		result.pop()
		return False
"""
In the solution, we can make this little faster by using cache for failed points
"""

#------------------------------------------------------------------------------
class TestClass(unittest.TestCase):
	def test_robot1(self):
		grid = [[0,0,0],[0,0,0],[0,0,0]]
		actual = robot_in_a_grid(grid)
		self.assertEqual([(0,0), (0,1), (0,2), (1,2), (2,2)], actual)
		grid = [[0,1,0],[0,0,0],[0,0,0]]
		actual = robot_in_a_grid(grid)
		self.assertEqual([(0,0), (1,0), (1,1), (1,2), (2,2)], actual)

	def test_triple_step1(self):
		actual = triple_step(6)
		self.assertEqual(24, actual)

	def test_triple_step2(self):
		actual = triple_step(5)
		self.assertEqual(13, actual)

if __name__ == "__main__":
	unittest.main()