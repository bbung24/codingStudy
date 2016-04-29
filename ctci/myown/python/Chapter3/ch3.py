#!/usr/bin/env python

'''
This file is for cracking the coding interview Chapter 3 : Stacks and Queues.
'''
#------------------------------------------------------------------------------
class StackWithMin(object):
	def __init__(self, storage = []):
		self.storage = storage
	def __repr__(self):
		return str(storage)
	def empty(self):
		return len(self.storage) == 0
	def push(self, value):
		if len(self.storage) == 0 or value < self.storage[-1][1]:
			self.storage.append((value, value))
		else:
			self.storage.append((value, self.storage[-1][1]))
	def pop(self):
		return self.storage.pop()[0]
	def peek(self):
		if len(self.storage) == 0: return None
		return self.storage[-1][0]
	def get_min(self):
		if len(self.storage) == 0: return None
		return self.storage[-1][1]

class Stack(list):
	def peak(self):
		return self[-1]
	def push(self, item):
		self.append(item)
	def empty(self):
		return len(self) == 0

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addFirst(self, value):
    	node = Node(value)
    	if self.head == None:
    		self.head = node
    		self.tail = node
    	else:
    		node.next = self.head
    		self.head = node

    def addLast(self,value):
        node = Node(value)
        #if the old list is none, set new node as the first node
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def __str__(self):
        if self.head != None:
            index = self.head
            nodestore = [str(index.value)]
            while index.next != None:
                index = index.next
                nodestore.append(str(index.value))
            return "LinkedList  [ " + "->".join(nodestore) + " ]"
        return "LinkedList  []"

    def __repr__(self):
        return self.__str__()

    def removeFirst(self):
    	if self.head == None:
    		return None
    	tmp = self.head
    	self.head = self.head.next
    	return tmp

    #remove the first node that have the same value as the given node_value
    def removeNode(self, node_value):
        current = self.head
        if current.value == node_value:
            self.head = self.head.next
        while(current.next != None):
            if current.next.value == node_value:
                current.next = current.next.next
                break
            else:
                current = current.next

#------------------------------------------------------------------------------
class singleArrayStacks(object):
	'''
	3.1
	Describe how you could use a single array to implement three stacks.
	'''

	def __init__(self, stacknum=3):
		self.stacknum = stacknum
		self.size = stacknum*100
		self.array = [0 for i in range(self.size)]
		self.pointer = [i*100 for i in range(stacknum)]

	def push(self, stacknum, elem):
		next_pt = self.pointer[stacknum] + 1
		limit = self.size/self.stacknum*(stacknum+1) 
		if next_pt >= limit:
			self.expandStack()

	# SKIP for now.

#------------------------------------------------------------------------------
# class minStack(object):
	'''
	3.2
	How would you design a stack which, in addition to push and pop, also has a
	function min which returns the minimum element? Push, pop and min should all
	operate in O(1) time.
	'''

#------------------------------------------------------------------------------
class SetOfStacks(object):
	'''
	3.3
	Imagine a (literal) stack of plates. If the stack gets too high, it might 
	topple. Therefore, in real life, we would likely start a new stack when
	the previous stack exceeds some threshold. 
	Implement a data structure SetOfStacks that mimics this. SetOfStacks
	should be composed of several stacks and should create a new stack once
	the previous one exceeds capacity. SetOfStacks' push() andSetOf Stacks'
	pop() should behave identically to a single stack (that is, pop() should
	return the same values as it would if there were just a single stack).
	
	FOLLOW UP

	Implement a function popAt(int index) which performs a pop operation on
	a specific sub-stack.
	'''
	stack = []
	cur_stack_num = 0

	def __init__(self, threshold=10):
		self.threshold = threshold

	def __repr__(self):
		return str(self.stack)

	def push(self, elem):
		if len(self.stack) == 0:
			self.stack.append([])
			self.cur_stack_num = 0
		elif len(self.stack[self.cur_stack_num]) == self.threshold:
			self.cur_stack_num += 1
			self.stack.append([])
		self.stack[self.cur_stack_num].append(elem)

	def pop(self):
		tmp = self.stack[self.cur_stack_num].pop()
		if len(self.stack[self.cur_stack_num]) == 0:
			self.cur_stack_num -= 1
			self.stack.pop()
		return tmp

	def popAt(self, index):
		# Check if index is valid substack that exists.
		tmp = self.stack[index].pop()
		if len(self.stack[index]) == 0:
			if self.cur_stack_num == index:
				self.cur_stack_num -= 1
				self.stack.pop()
			else:
				self.cur_stack_num -= 1
				del self.stack[index]
		return tmp

#------------------------------------------------------------------------------
class TowersOfHanoi(object):
	'''
	3.4
	In the classic problem of the Towers of Hanoi, you have 3 towers and
	N disks of different sizes which can slide onto any tower. The puzzle
	starts with disks sorted in ascending order of size from top to bottom 
	(i.e., each disk sits on top of an even larger one). 
	You have the following constraints:
		(1) Only one disk can be moved at a time.
		(2) A disk is slid off the top of one tower onto the next tower.
		(3) A disk can only be placed on top of a larger disk.
	Write a program to move the disks from the first tower to the last using
	stacks.
	'''

	def __init__(self, size):
		self.towers = [[],[],[]]
		self.size = size
		# self.towers[0] = [for i in range(size, 0, -1)]

	def __repr__(self):
		return str(self.towers)

	def printTowers(self):
		print str(self.towers)

	def playHanoi(self):
		''' Let's finish this later since I already saw the answer '''
		return


#------------------------------------------------------------------------------
class MyQueue(object):
	'''
	3.5
	Implement a MyQueue class which implements a queue using two stacks.
	'''

	def __init__(self):
		self.push_stack = StackWithMin()
		self.pop_stack = StackWithMin()

	def push(self, elem):
		if self.push_stack.empty() and not self.pop_stack.empty():
			self.moveStack(self.pop_stack, self.push_stack)
		self.push_stack.push(elem)

	def pop(self):
		if self.pop_stack.empty() and not self.push_stack.empty():
			self.moveStack(self.push_stack, self.pop_stack)
		return self.pop_stack.pop()

	def moveStack(self, From, To):
		elem = From.pop()
		To.push(elem)

#------------------------------------------------------------------------------
def sortStack(stack):
	'''
	3.6
	Write a program to sort a stack in ascending order (with biggest items on top).
	You may use at most one additional stack to hold items, but you may not copy 
	the elements into any other data structure (such as an array). The stack supports 
	the following operations: push, pop, peek, and isEmpty.
	'''
	# Let's do this later again because I saw the answer and mine doesn't work with 
	# duplicate numbers.
	def moveStack(From, to):
		while not From.empty():
			temp = From.pop()
			to.push(temp)

	def checkMax(stack, hold):
		max_num = None
		while not stack.empty():
			temp = stack.pop()
			if max_num == None or temp > max_num:
				max_num = temp
			hold.push(temp)
		moveStack(hold, stack)
		return max_num

	def moveExcept(stack, hold, excpt):
		hold_elem = None
		while not stack.empty():
			temp = stack.pop()
			if temp == excpt:
				hold_elem = temp
			else:
				hold.push(temp)
		stack.push(hold_elem)
		moveStack(hold, stack)

	hold = StackWithMin()
	max_num = checkMax(stack, hold)
	for i in range(max_num):
		moveExcept(stack, hold, i)

#------------------------------------------------------------------------------
class Animal(object):
	def __init__(self, kind, name):
		self.kind = kind
		self.name = name

class Shelter(object):
	'''
	3.7
	An animal shelter holds only dogs and cats, and operates on a strictly 
	"first in, first out" basis. People must adopt either the "oldest" 
	(based on arrival time) of all animals at the shelter, or they can select 
	whether they would prefer a dog or a cat (and will receive the oldest animal 
	of that type). They cannot select which specificanimal they would like. 
	Create the data structures to maintain this system and implement operations 
	such as enqueue, dequeueAny, dequeueDog and dequeueCat.
	You may use the built-in LinkedList data structure
	'''

	def __init__(self):
		self.animals = LinkedList()

	def __str__(self):
		return str(self.animals)

	def __repr__(self):
		return self.__str__()

	def enqueue(self, animal):
		self.animals.addLast(animal)

	def dequeueAny(self):
		return self.animals.removeFirst().value

	def dequeueDog(self):
		tmp = self.animals.removeFirst()
		stack = Stack()
		if tmp != None and tmp.value.kind != 'Dog':
			stack.push(tmp.value)
		while tmp != None and tmp.value.kind != 'Dog':
			tmp = self.animals.removeFirst()
			if tmp != None and tmp.value.kind != 'Dog':
				stack.push(tmp.value)
		while not stack.empty():
			self.animals.addFirst(stack.pop())
		return tmp.value

	def dequeueCat(self):
		tmp = self.animals.removeFirst()
		stack = Stack()
		if tmp != None and tmp.value.kind != 'Cat':
				stack.push(tmp.value)
		while tmp != None and tmp.value.kind != 'Cat':
			tmp = self.animals.removeFirst()
			if tmp != None and tmp.value.kind != 'Cat':
				stack.push(tmp.value)
		while not stack.empty():
			self.animals.addFirst(stack.pop())
		return tmp.value















































