"""
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, 
which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container. 

"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        left = 0
        right = len(height)-1
        for w in range(len(height)-1, 0, -1):
            if height[left] < height[right]:
                maxArea = max(maxArea, height[left] * w)
                left = left + 1
            else:
                maxArea = max(maxArea, height[right] * w)
                right = right - 1
        return maxArea

if __name__ == "__main__":
    test = Solution()
    result = test.maxArea([1,2])
    print result == 1
    result = test.maxArea([1,2])
    print result == 1