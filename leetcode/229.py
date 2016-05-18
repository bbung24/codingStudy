"""
229. Majority Element II

Given an integer array of size n, find all elements that appear more than lower_bound(n/3)  times. 
The algorithm should run in linear time and in O(1) space.

Hint:

    How many majority elements could it possibly have?
        Max 2

"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        bar = len(nums) // 3
        counts = {}
        for num in nums:
            if not num in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        largest1 = largest2 = None
        largest_count1 = largest_count2 = 0
        for num in counts:
            if counts[num] >= largest_count1:
                if largest_count1 >= largest_count2:
                    largest2 = largest1
                    largest_count2 = largest_count1
                largest1 = num
                largest_count1 = counts[num]
            elif counts[num] >= largest_count2:
                largest2 = num
                largest_count2 = counts[num]
        result = []
        if largest1 != None and largest_count1 > bar:
            result.append(largest1)
        if largest2 != None and largest_count2 > bar:
            result.append(largest2)
        return result

    def not_so_good(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        currentNum = None
        bar = len(nums) / 3
        nums.sort()
        index = 0
        result = []
        while index < len(nums):
            num = nums[index]
            if num != currentNum and index+bar < len(nums) and nums[index+bar] == num:
                currentNum = num
                result.append(num)
                if len(result) == 2:
                    break
                index += 1
            else:
                del nums[index]
        return result

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
    result = test.majorityElement([1,2,3])
    # Should print []
    print result