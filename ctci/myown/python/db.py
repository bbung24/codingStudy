#!/usr/bin/env python

'''
This file is for cracking the coding interview database utility.
'''

class LNode:
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

    def addNode(self,value):
        node = LNode(value)
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

class TNode(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.parent = None
    def __str__(self):
        return "TNode("+str(self.value)+")"
    def __repr__(self):
        return self.__str__()

class BinaryTree(object):
    def __init__(self):
        self.root = None

class DirectedTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def __str__(self):
        return 'DirectedTree('+str(self.value)+'):'+str(self.neighbors)

    def __repr__(self):
        return self.__str__()