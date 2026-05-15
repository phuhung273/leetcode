"""
Problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
Idea: Binary search: if mid is increasing, find left. Else find right
Return when mid >= mid - 1 and mid >= mid + 1
Time: O(logN)
Space: O(1)
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                return nums[mid]
            elif nums[left] <= nums[mid] <= nums[right]:
                return nums[left]
            elif nums[mid] <= nums[right] <= nums[left]:
                right = mid
            else:
                left = mid + 1
        return nums[left]

sol = Solution()
sol.findMin([2,3,4,5,1]) # 1
sol.findMin([2,1]) # 1
sol.findMin([1]) # 1
sol.findMin([1,1]) # 1
sol.findMin([1,1,1]) # 1
sol.findMin([3,4,5,1,2]) # 1
sol.findMin([1,2,3,4,5]) # 1
sol.findMin([4,5,6,7,0,1,2]) # 0
sol.findMin([11,13,15,17]) # 11
