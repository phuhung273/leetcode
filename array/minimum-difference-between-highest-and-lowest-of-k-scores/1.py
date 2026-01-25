# type: ignore
"""
Problem: https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores

Idea: Sort and iterate. Compare ans with nums[i] and nums[i + k]
Time: O(sortN)
Space: O(sortN)

Idea: Keep a sortedlist (BST underneath) of size k
When list is full, if item is within min and max of list, binary search and insert it in the list.
Compare and remove first or last item.
Time: O(NlogK)
Space: O(k)
=> Wrong, because at the beginning, we might be adding incorrect chosen items. But correct items might be out of range and eliminate
"""

import math
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0

        nums.sort()
        ans = math.inf
        for i in range(len(nums) - k + 1):
            ans = min(ans, nums[i + k - 1] - nums[i])
        return ans

sol = Solution()
sol.minimumDifference(nums = [93614,91956,83384,14321,29824,89095,96047,25770,39895], k = 3)
sol.minimumDifference(nums = [87063,61094,44530,21297,95857,93551,9918], k = 6)
sol.minimumDifference(nums = [9,4,1,7], k = 2)
sol.minimumDifference(nums = [90], k = 1)
