"""
Problem: https://leetcode.com/problems/house-robber
Idea: DP, dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
Time: O(N)
Space: O(1)
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            curr = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = curr
        return prev1

sol = Solution()
sol.rob([1,2,3,1]) # 4
sol.rob([2,7,9,3,1]) # 12
