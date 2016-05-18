# -*- coding: utf-8 -*-
"""
169. Majority Element

Given an array of size n, find the majority element. 

The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
        	return None
        nums.sort()
        return nums[len(nums)/2]

if __name__ == "__main__":
    test = Solution()
    result = test.majorityElement([])
    # Should print []
    print result
    result = test.majorityElement([1,1,1,1,1,1,1,1,1])
    # Should print 1
    print result
    result = test.majorityElement([1,1,1,4,5])
    # Should print 1
    print result