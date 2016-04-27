#!/usr/bin/env python

'''
This file is for cracking the coding interview Chapter 5 : Bit Manipulation.
'''

#------------------------------------------------------------------------------
def getBit(num, i):
	'''get bit of given position i'''
	return int((num & (1 << i)) != 0)

#------------------------------------------------------------------------------
def setBit(num, i):
	'''set bit of given position i'''
	return num | (1 << i)

#------------------------------------------------------------------------------
def clearBit(num, i):
	'''clear bit of given position i'''
	return num & ~(1 << i)

#------------------------------------------------------------------------------
def updateBit(num, i, b):
	'''update bit of given position i with given bit b'''
	num = clearBit(num, i)
	if b == 1:
		num = setBit(num, i)
	return num

#------------------------------------------------------------------------------
def putBinary(N, M, i, j):
	'''
	5.1
	You are given two 32-bit numbers, N and M, and two bit positions, i and j.
	Write a method to insert M into N such that M starts at bit j and ends at bit i.
	You can assume that the bits j through i have enough space to fit all of M.
	That is, if M = 10011, you can assume that there are at least 5 bits between j and i.
	You would not, for example, have j = 3 and i = 2, because M could not fully fit between
	bit 3 and bit 2.
	
	EXAMPLE
	Input : N = 10000000000, M = 10011, i = 2, j = 6
	Output: N = 10001001100
	'''
	result = N
	for index, bit in enumerate(bin(M).split('b')[1][::-1]):
		result = updateBit(result, i+index, int(bit))
	return result


