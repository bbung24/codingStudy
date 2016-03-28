"""
Count of Smaller Numbers After Self

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i]. 

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

Return the array [2, 1, 1, 0]. 
"""
class Solution(object):
    # def betterCountSmaller(self, nums):

    def __init__(self):
        import numpy.random as nprnd
        self.test_list = nprnd.randint(1000, size=10000)

    def anotherTry(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rank, N, res = {val: i + 1 for i, val in enumerate(sorted(nums))}, len(nums), []
        BITree = [0] * (N + 1)

        def update(i):
            while i <= N:
                BITree[i] += 1
                i += (i & -i)

        def getSum(i):
            s = 0
            while i:
                s += BITree[i]
                i -= (i & -i)
            return s

        for x in reversed(nums):
            res += getSum(rank[x] - 1),
            update(rank[x])
        return res[::-1]

    def betterCountSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0] * len(nums)
        for index, num in enumerate(nums):
            result[index] = len([n for n in nums[index+1:] if n < num])
        return result

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0] * len(nums)
        for index, num in enumerate(nums):
            count = 0
            for compare in nums[index+1:]:
                if compare < num:
                    count += 1
            result[index] = count
        return result

    def better_test(self):
        print self.betterCountSmaller(self.test_list)
    def test(self):
        print self.countSmaller(self.test_list)
    def another_test(self):
        print self.anotherTry(self.test_list)

if __name__ == "__main__":
    test = Solution()
    # print test.betterCountSmaller([5,6,2,1,7,8])
    # print test.countSmaller([5,6,2,1,7,8])
    # print test.anotherTry([5,6,2,1,7,8])
    import timeit
    print timeit.Timer(test.better_test).timeit(number=1)
    print timeit.Timer(test.test).timeit(number=1)
    print timeit.Timer(test.another_test).timeit(number=1)
    

