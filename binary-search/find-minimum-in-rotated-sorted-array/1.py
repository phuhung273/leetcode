"""
Problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

Idea:
If mid is greater than right, mid is on the right side of the array. Left = mid + 1
Else right = mid
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

sol = Solution()
sol.findMin([4,5,1,2,3])
sol.findMin([3,4,5,1,2])
sol.findMin([4,5,6,7,0,1,2])
sol.findMin([11,13,15,17])
