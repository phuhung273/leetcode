"""
Problem: https://leetcode.com/problems/maximum-total-subarray-value-i
Idea: (max - min) * k
Time: O(N)
Space: O(1)
"""

import math
from typing import List


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        minimum = nums[0]
        maximum = nums[0]

        for num in nums:
            if num > maximum:
                maximum = num
            elif num < minimum:
                minimum = num
        return (maximum - minimum) * k

sol = Solution()
sol.maxTotalValue(nums = [1,3,2], k = 2)
sol.maxTotalValue(nums = [4,2,5,1], k = 3)
