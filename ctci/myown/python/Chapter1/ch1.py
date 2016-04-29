#!/usr/bin/env python

'''
This file is for cracking the coding interview Chapter 1 : Arrays and String
'''

#------------------------------------------------------------------------------
def all_unique(input):
    '''
    1.1
    Implement an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structures?
    '''
    if len(input) == 0:
        return True
    char = None
    for c in sorted(input):
        if char == c:
            return False
        char = c
    return True

#------------------------------------------------------------------------------
def revStr(str):
    '''
    1.2 
    Implement a function voci reverse(char* str) in C or C++ which reverses
    a null-terminated string.
    '''
    # newStr = ''
    # for c in str:
    #   newStr = c + newStr
    # return newStr
    # CORRECT WAY
    if str != "":
        return str[-1:] + revStr[:-1]
    else:
        return ""

#------------------------------------------------------------------------------
def anagram(one, two):
    '''
    1.3 
    Given two strings, write a method to decide if one is a permutation of
    the other.
    '''
    one = one.replace(' ','').lower() # NOTE: I need to ask about these cases 
                                      # to find out they can become permutation.
    two = two.replace(' ','').lower()
    if len(one) != len(two):
        return False
    if one == two:
        return True
    for c in set(one):
        if one.count(c) != two.count(c):
            return False
    return True

#------------------------------------------------------------------------------
def replaceSpaces(orig):
    '''
    1.4
    Write a method to replace all spaces in a string with '%20'. You may assume
    that the string has sufficient space at the end of the string to hold the
    additional characters, and that you are given the "true" length of the
    string. (Note: if implementing in JAVA, please use a character array so 
    that you can perform this operation in place.)
    EXAMPLE 
    input : "Mr John Smith    "
    output: "Mr%20John%20Smith"
    '''
    return ' '.join(orig.split()).replace(' ', '%20')
    # even better : '%20'.join(orig.split())

#------------------------------------------------------------------------------
def compress(inStr):
    '''
    1.5
    Implement a method to perform basic string compression using the counts of
    repeated characters. For example, the string aabcccccaaa would become
    a2b1c5a3. If the "compressed" string would not become smaller than the 
    original string, your method should return the original string.
    '''
    newStr = []
    if len(inStr) == 0:
        return ''
    prev = inStr[0]
    count = 1
    for c in inStr[1:]:
        if c != prev:
            newStr.append(prev)
            newStr.append(str(count))
            prev = c
            count = 1
        else:
            count += 1
    newStr.append(prev)
    newStr.append(str(count))
    newStr = ''.join(newStr)
    if len(newStr) > len(inStr):
        return inStr
    else:
        return newStr

    # NOTE: there is a python function itertools.groupby which does exactly 
    # same thing that we are tring to do here.

#------------------------------------------------------------------------------
def rotate(image):
    '''
    1.6
    Given an image represented by an NxN matrix, where each pixel in the image
    is 4 bytes, write a method to rotate the image by 90 degrees. Can you do 
    this in place?
    input = [[]] ; output[[]]
    input = [[1,2],[3,4]] ; output = [[4,1],[3,2]]
    input = [[1,2,3],[4,5,6],[7,8,9]] ; output = [[7,4,1],[8,5,2],[9,6,3]]
    input = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]] ;
    output = [[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]]
    '''
    if len(image) < 2:
        return image
    N = len(image)
    print N
    start = 0
    end = N
    for row in range(start, end/2):
        print row
        print start, end
        for col in range(start, end-1):
            print col
            print image
            tmp = image[row][col]
            image[row][col] = image[end-1-col][row]
            image[end-1-col][row] = image[end-1-row][end-1-col]
            image[end-1-row][end-1-col] = image[col][end-1-row]
            image[col][end-1-row] = tmp
            print image
        start += 1
        end -= 1
    return image

#------------------------------------------------------------------------------
def zeroProcess(matrix):
    '''
    1.7
    Write an algorithm such that if an element in an MxN matrix is 0, its
    entire row and column are set to 0.
    input = [[]] ; output = [[]]
    input = [[1,0]] ; output = [[0,0]]
    '''
    # Pseudocode
    # Let's first check if the matrix is even needed to process. 
    # If matrix is 1x1 or less in length, don't even need to look through.
    if len(matrix) == 0 or (len(matrix) <= 1 and len(matrix[0]) <= 1):
        return matrix
    new_matrix = [[-1 for y in range(len(matrix[0]))] 
                    for x in range(len(matrix))]
    # Go through MxN matrix
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[0])):
            if matrix[row][col] == 0:
                zeroRow(new_matrix, row)
                zeroCol(new_matrix, col)
            elif new_matrix[row][col] == -1:
                new_matrix[row][col] = matrix[row][col]
    return new_matrix

def zeroRow(matrix, x):
    '''
    Helper function for zeroProcess. 
    Will replace all elements in x row to zero.
    '''
    for col in range(0, len(matrix[x])):
        matrix[x][col] = 0

def zeroCol(matrix, y):
    '''
    Helper function for zeroProcess.
    Will replace all elements in y col to zero.
    '''
    for row in range(0, len(matrix)):
        matrix[row][y] = 0

#------------------------------------------------------------------------------
def isRotate(s1, s2):
    '''
    1.8
    Assume you have a method isSubstring which checks if one word is a
    substring of another. Given two strings, s1 and s2, write code to check
    if s2 is a rotation of s1 using only one call to isSubstring (e.g., 
    "waterbottle" is a rotation of "erbottlewat")
    '''
    # if len(s1) < 1 or len(s2) < 1:
    #   return False
    if len(s1) != len(s2):
        return False
    # if s1 == s2:# Do I need to ask if same string is rotation of each other ?
    #   return True
    # check_word = s1[len(s1)] + s1[0]
    # rotate_point = s2.find(check_word)
    # if rotate_point > len(s1)/2:
    #   return isSubstring(s2[0:rotate_point], s1)
    # else:
    #   return isSubstring(s2[rotate_point:], s1)
    # I'm so stupid !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    new_string = s2 + s2
    return isSubstring(new_string, s1)

def isSubstring(word, string):
    '''
    checks if one word is a substring of another.
    '''
    if word in string:
        return True
    else:
        return False






































