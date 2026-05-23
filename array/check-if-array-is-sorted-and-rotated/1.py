"""
Problem: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated
Idea:
Whenever encountering decreasing element, break, its index is minIndex
Do another for loop in range [minIndex, n + minIndex] to check non-decreasing
Time: O(N)
Space: O(1)
---------------------------------------------------------------------------------
Idea: Check from 0 to n + 1 to find number of local minimum
Time: O(N)
Space: O(1)
"""

from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        foundLocalMinimum = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if foundLocalMinimum:
                    return False
                foundLocalMinimum = True

        if foundLocalMinimum:
            return nums[-1] <= nums[0]
        return True

    # def check(self, nums: List[int]) -> bool:
    #     n = len(nums)
    #     minIndex = -1

    #     for i in range(1, len(nums)):
    #         if nums[i] < nums[i - 1]:
    #             minIndex = i
    #             break
        
    #     if minIndex != -1:
    #         last = nums[minIndex]
    #         for i in range(minIndex + 1, minIndex + n):
    #             index = i % n
    #             if nums[index] < last:
    #                 return False
    #             last = nums[index]

    #     return True

sol = Solution()
sol.check([5,1,2,3,4]) # T
sol.check([3,4,5,1,2]) # T
sol.check([2,1,3,4]) # F
sol.check([1,2,3]) # T
sol.check([1,1,1]) # T
sol.check([1,1]) # T
sol.check([1]) # T
