"""
Idea: Recursion with memo
f(i) =  min(f(i-1) + cost[i - 1], f(i-2) + cost[i - 2])
Base case: if i == 0 or i == 1, f(i) = 0

Time: O(N) since we have cache, each i is only calculated once
Space: O(N) = N(height of recursion stack) * 3(input i + local lastOne + local lastTwo) + N(cache)
"""

from functools import cache
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def climb(i: int) -> int:
            if i in [0, 1]:
                return 0
            lastOne = climb(i - 1) + cost[i - 1]
            lastTwo = climb(i - 2) + cost[i - 2]
            return min(lastOne, lastTwo)
        
        return climb(len(cost))

sol = Solution()
result = sol.minCostClimbingStairs([10,15,20]) # 15
result = sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]) # 6
print('test')
