"""
229. Majority Element II

Given an integer array of size n, find all elements that appear more than lower_bound(n/3)  times. 
The algorithm should run in linear time and in O(1) space.

"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        currentNum = None
        bar = len(nums) / 3
        nums.sort()
        index = 0
        while index < len(nums):
            num = nums[index]
            if num != currentNum and index+bar < len(nums) and nums[index+bar] == num:
                currentNum = num
                index += 1
            else:
                del nums[index]
        return nums

if __name__ == "__main__":
    test = Solution()
    result = test.majorityElement([])
    # Should print []
    print result
    result = test.majorityElement([1,1,1,1,1,1,1,1,1])
    # Should print [1]
    print result
    result = test.majorityElement([1,1,3,4,5])
    # Should print [1]
    print result