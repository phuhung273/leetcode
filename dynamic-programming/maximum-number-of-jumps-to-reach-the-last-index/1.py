"""
Problem: https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index
Idea:
From i, iterate to end of arr to find all possible j. Then continue to j. TC: O(N^2)
---
Put all in BST.
With every i, go to child or parent >> Child or parent ???
---
DP: for each j, iterate all i < j. Set dp[j] = max(dp[j], dp[i] + 1) if target abs(nums[i] - nums[j]) < target

Time: O(N^2)
Space: O(N)
"""

from typing import List


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0

        for j in range(n):
            for i in range(j):
                if dp[i] != -1 and abs(nums[i] - nums[j]) <= target:
                    dp[j] = max(dp[j], dp[i] + 1)
        return dp[n - 1]

sol = Solution()
sol.maximumJumps(nums = [0,2,1,3], target = 1) # -1
sol.maximumJumps(nums = [1,3,6,4,1,2], target = 2) # 3
sol.maximumJumps(nums = [1,3,6,4,1,2], target = 3) # 5
sol.maximumJumps(nums = [1,3,6,4,1,2], target = 0) # -1
