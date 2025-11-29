"""
Problem: https://leetcode.com/problems/sort-an-array

Idea: basic selection sort

Time: O(N^2)
Space: O(1)
"""

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            smallest = nums[i]
            idx = i
            for j in range(i + 1, len(nums)):
                if nums[j] < smallest:
                    smallest = nums[j]
                    idx = j
            nums[idx] = nums[i]
            nums[i] = smallest

        return nums

sol = Solution()
sol.sortArray([5,2,3,1])
sol.sortArray([5,1,1,2,0,0])
