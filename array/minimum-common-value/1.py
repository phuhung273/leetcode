"""
Problem: https://leetcode.com/problems/minimum-common-value
Idea: Have 2 pointers p1 and p2. Increase whichever is smaller until end of array
Time: O(max(M, n))
Space: O(1)
"""

from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        p1 = p2 = 0

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                return nums1[p1]
            if nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return -1

sol = Solution()
sol.getCommon(nums1 = [1], nums2 = [2]) # -1
sol.getCommon(nums1 = [2], nums2 = [2,4]) # 2
sol.getCommon(nums1 = [2], nums2 = [2]) # 2
sol.getCommon(nums1 = [1,2,3], nums2 = [2,4]) # 2
sol.getCommon(nums1 = [1,2,3], nums2 = [4,5]) # -1
sol.getCommon(nums1 = [1,2,3,6], nums2 = [2,3,4,5]) # 2
