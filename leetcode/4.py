"""
4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively. 
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

My NOTE:

If n is odd then Median (M) = value of ((n + 1)/2)th item term.

If n is even then Median (M) = value of [((n)/2)th item term + ((n)/2 + 1)th item term ]/2

"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        full_list = sorted(nums1 + nums2)
        n = len(nums1) + len(nums2)
        if n % 2 == 0:
            return (full_list[n/2-1]+full_list[n/2])/2.0
        else:
            return full_list[n/2]

if __name__ == "__main__":
    test = Solution()
    # import numpy.random as nprnd
    # test_list1 = nprnd.randint(100, size=10)
    # test_list2 = nprnd.randint(100, size=20)
    test_list1 = [1, 2, 4, 7, 10]
    test_list2 = [3, 5, 6, 8, 9]
    print test.findMedianSortedArrays(test_list1, test_list2)