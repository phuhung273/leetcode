"""
Problem: https://leetcode.com/problems/partition-array-according-to-given-pivot
Idea:

Iterate, add all less to less, greater to greater. In the end, build the ans arr

Time: O(N)
Space: O(N)
"""

from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        greater = []

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)

        for _ in range(len(nums) - len(less) - len(greater)):
            less.append(pivot)
        less.extend(greater)
        return less

sol = Solution()
sol.pivotArray(nums = [9,12,5,10,14,3,10], pivot = 10) # [9,5,3,10,10,12,14]
sol.pivotArray(nums = [-3,4,3,2], pivot = 2) # [-3,2,4,3]
