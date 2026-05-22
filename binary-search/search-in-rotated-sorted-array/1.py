"""
Problem: https://leetcode.com/problems/search-in-rotated-sorted-array
Idea: Binary search to find the minimum first
If mid < mid + 1 and mid < mid - 1, return mid
If left < right, return left
Elif mid > right, left = mid + 1
Elif mid < right < left, right = mid

Then compare target with min and bisect_left target in left or right array
Time: O(logN)
Space: O(1)
"""

import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minIndex = findMinIndex(nums)

        idx = -1
        if nums[len(nums) - 1] >= target >= nums[minIndex]:
            idx = bisect.bisect_left(nums, lo=minIndex, x=target)
        elif nums[0] <= target <= nums[minIndex - 1]:
            idx = bisect.bisect_left(nums, hi=minIndex, x=target)
        
        return idx if nums[idx] == target else -1

def findMinIndex(nums: List[int]) -> int:
    if len(nums) == 1:
        return 0

    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] < nums[right]:
            return left
        
        mid = left + (right - left) // 2

        if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
            return mid
        elif nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return left

sol = Solution()
sol.search(nums = [3,1], target = 3) # 0
sol.search(nums = [3,1], target = 1) # 1
sol.search(nums = [1,3], target = 2) # -1
sol.search(nums = [1], target = 1) # 0
sol.search(nums = [4,5,6,7], target = 4) # 0
sol.search(nums = [4,5,6,7], target = 7) # 3
sol.search(nums = [4,5,6,7,0,1,2], target = 0) # 4
sol.search(nums = [4,5,6,7,0,1,2], target = 3) # -1
sol.search(nums = [1], target = 0) # -1
sol.search(nums = [4,5,6,7,0,1,2], target = 8) # -1
