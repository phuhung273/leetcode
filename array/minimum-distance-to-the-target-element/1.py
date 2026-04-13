"""
Problem: https://leetcode.com/problems/minimum-distance-to-the-target-element
Idea: Iterate and compare
Optimization: early exist i - start > ans
Time: O(N)
Space: O(1)
"""

import math
from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        if len(nums) == 0:
            return 0

        ans = math.inf
        for i, num in enumerate(nums):
            if i - start > ans:
                break
            if num != target:
                continue

            ans = min(ans, abs(i - start))
        return ans # type: ignore

sol = Solution()
sol.getMinDistance(nums = [1,2,3,4,5], target = 5, start = 3) # 1
sol.getMinDistance(nums = [1], target = 1, start = 0) # 0
sol.getMinDistance(nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0) # 0
