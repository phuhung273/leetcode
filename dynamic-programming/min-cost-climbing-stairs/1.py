"""
Problem: https://leetcode.com/problems/min-cost-climbing-stairs
Idea: dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + + cost[i - 1])
Time: O(N)
Space: O(1)
"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost[0], cost[1])

        dp2 = 0
        dp1 = 0
        
        for i in range(2, len(cost) + 1):
            dp = min(dp2 + cost[i - 2], dp1 + cost[i - 1])
            dp2 = dp1
            dp1 = dp
        return dp1

sol = Solution()
sol.minCostClimbingStairs([10,15,20]) # 15
sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]) # 6
