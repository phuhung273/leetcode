"""
Problem: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element
Idea: Save index of last zero as left
When encountering next zero, calculate max and set left = zero + 1
Time: O(N)
Space: O(1)
"""

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right, zero = 0, 0, -1
        ans = 0
        while right < len(nums):
            while right < len(nums) and nums[right]:
                right += 1
            
            # Encounter 1st zero
            if zero == -1:
                zero = right
                right += 1
                continue

            ans = max(ans, right - left - 1)
            left = zero + 1
            zero = right
            right += 1
        return ans if left != 0 else len(nums) - 1

sol = Solution()
# sol.longestSubarray([1,1,0,1]) # 3
# sol.longestSubarray([0,1,1,0,1]) # 3
# sol.longestSubarray([0,1,1,1,0,1,1,0,1]) # 5
sol.longestSubarray([1,1,1]) # 2
