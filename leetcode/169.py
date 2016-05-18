# -*- coding: utf-8 -*-
"""
169. Majority Element

Given an array of size n, find the majority element. 

The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

"""
class Solution(object):
    def majorityElementWithLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = None
        largest_count = 0
        for num in nums:
            if largest == None:
                largest = num
                largest_count = 1
            elif num != largest:
                largest_count -= 1
            else:
                largest_count += 1
            if largest_count == 0:
                largest = num
                largest_count = 1
        return largest
                
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums)/2]

if __name__ == "__main__":
    test = Solution()
    result = test.majorityElement([1,1,1,1,1,1,1,1,1])
    # Should print 1
    print result
    result = test.majorityElement([1,1,1,4,5])
    # Should print 1
    print result