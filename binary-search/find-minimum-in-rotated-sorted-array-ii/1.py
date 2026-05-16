"""
Problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii
Idea: Binary search
If mid < its left and right, return
ElIf mid < left, right = mid
Elif mid > right, left = mid
Else: call recursively left part and right part
l       m       r
2   2   2   0   1

        l   m   r
2   2   2   0   1

l       m       r
2   2   2   1   2

Time:
Space:
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = findMin(nums, 0, len(nums) - 1)
        return ans
        
    
def findMin(nums: List[int], left: int, right:int) -> int:
    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < nums[mid - 1]:
            return nums[mid]
        elif nums[mid] > nums[right]:
            left = mid + 1
        elif nums[mid] < nums[left]:
            right = mid
        else:
            leftMin = findMin(nums, left=left, right=mid)
            rightMin = findMin(nums, left=mid + 1, right=right)
            return min(leftMin, rightMin)
    return nums[left]


sol = Solution()
sol.findMin([2,2,2,0,2])
sol.findMin([1,3,5])
sol.findMin([2,2,2,0,1])
sol.findMin([4,5,6,7,0,1,4])
sol.findMin([0,1,4,4,5,6,7])

sol.findMin([2,3,4,5,1]) # 1
sol.findMin([2,1]) # 1
sol.findMin([1]) # 1
sol.findMin([1,1]) # 1
sol.findMin([1,1,1]) # 1
sol.findMin([3,4,5,1,2]) # 1
sol.findMin([1,2,3,4,5]) # 1
sol.findMin([4,5,6,7,0,1,2]) # 0
sol.findMin([11,13,15,17]) # 11
