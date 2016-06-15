#!/usr/bin/env python

'''
This file is for cracking the coding interview Chapter 6 : Math and logic puzzles.
'''
# Examplify, Simplify, Generalize, Pattern matching, and Base Case and build.
#------------------------------------------------------------------------------
def findHeavyBottle():
	'''
	6.1
	You have 20 bottles of pills. 19 bottles have 1.0 gram pills, but one has pills 
	of weight 1.1 grams. Given a scale that provides an exact measurement, how
	would you find the heavy bottle? You can only use the scale once.
	'''
	"""
	Take one pill from first bottle. Take two pills from second bottle and so forth.
	If the sum is 20.1, heavy bottle is first bottle. 20.2 = second, 21.0 = 10th,
	22.0 = 20th, etc.
	CORRECT
	"""

"""
6.2 Basketball
You have a basketball hoop and someone says that you can play one of two games.
Game 1: You get one shot to make the hoop.
Game 2: You get three shots and you have to make two fo three shots.
If p is the probability of making a particular shot, for which values of p should
you pick one game or the other? 
"""
"""
See Ipad for an answer.
"""
