"""
Problem: https://leetcode.com/problems/sort-colors

Idea: Quick sort 1
Time: O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        pointer = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = nums[pointer]
                nums[pointer] = 0
                pointer += 1

        pointer = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 2:
                nums[i] = nums[pointer]
                nums[pointer] = 2
                pointer -= 1
        return



sol = Solution()
sol.sortColors([2,0,2,1,1,0])
