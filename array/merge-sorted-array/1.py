"""
Problem: https://leetcode.com/problems/merge-sorted-array

Idea: Start with j = len(nums1) - 1, k = len(nums2) - 1. Traverse backward

Time: O(m + n)
Space: O(1)
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        
        m -= 1
        n -= 1

        for k in range(len(nums1) - 1, -1, -1):
            if m == -1:
                nums1[k] = nums2[n]
                n -= 1
            elif n == -1:
                break
            elif nums1[m] > nums2[n]:
                nums1[k] = nums1[m]
                m -= 1
            else:
                nums1[k] = nums2[n]
                n -= 1


sol = Solution()
# sol.merge(nums1 = [4,5,6,0,0,0], m = 3, nums2 = [1,2,3], n = 3)
# sol.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [4,5,6], n = 3)
# sol.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# sol.merge(nums1 = [1], m = 1, nums2 = [], n = 0)
sol.merge(nums1 = [0], m = 0, nums2 = [1], n = 1)
