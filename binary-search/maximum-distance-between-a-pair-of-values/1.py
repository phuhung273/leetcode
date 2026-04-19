"""
Problem: https://leetcode.com/problems/maximum-distance-between-a-pair-of-values
Idea:
For every i, binary search from i to end
Time: O(NlogM)
Space: O(1)
"""

import bisect
from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        for i, num in enumerate(nums1):
            j = bisect.bisect_right(nums2, -num, lo=i, key=lambda x: -x)

            # Stop early when less than end of nums2
            if j == len(nums2):
                ans = max(ans, j - i - 1)
                break

            if num == nums2[j]:
                ans = max(ans, j - i)
            else:
                ans = max(ans, j - i - 1)

        return ans

sol = Solution()
sol.maxDistance(nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]) # 2
sol.maxDistance(nums1 = [2,2,2], nums2 = [10,10,3]) # 2
sol.maxDistance(nums1 = [2,2,2], nums2 = [10,10,1]) # 1
sol.maxDistance(nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]) # 2
