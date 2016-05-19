# -*- coding: utf-8 -*-
"""
242. Valid Anagram

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
          return False
        chars = {}
        for c in s:
          if not c in chars:
            chars[c] = 1
          else:
            chars[c] += 1
        for c in t:
          if not c in chars:
            return False
          else:
            chars[c] -= 1
            if chars[c] == 0:
              del chars[c]
        if len(chars.keys()) == 0:
          return True
        else:
          return False

if __name__ == "__main__":
    test = Solution()
    result = test.isAnagram('','')
    # Should print True
    print result
    result = test.isAnagram('rat', 'car')
    # Should print False
    print result
    result = test.isAnagram('anagram', 'nagarm')
    # Should print False
    print result