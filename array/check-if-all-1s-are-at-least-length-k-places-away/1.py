"""
Problem: https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away
"""

from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = None
        for i, num in enumerate(nums):
            if num == 0:
                continue
            if last is None or i - last > k:
                last = i
                continue
            return False
        return True

sol = Solution()
sol.kLengthApart(nums = [1,0,0,0,1,0,0,1], k = 2)
sol.kLengthApart(nums = [1,0,0,1,0,0,1], k = 2)
sol.kLengthApart(nums = [1,0,0,0,0,0,1], k = 2)
sol.kLengthApart(nums = [1,0,1,0,0,0,1], k = 2)
sol.kLengthApart(nums = [1,0,0,1,0,1,1], k = 2)
sol.kLengthApart(nums = [1,0,0,1,0,1], k = 2)
