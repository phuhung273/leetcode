"""
Problem: https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount
Idea: Sort and buy from the end
1   2   2   5   6   7   9

1st way with 9: (9 + 7) + (5 + 2) + (1) = 24
2nd way without 9: 9 + (7 + 6) + (2 + 2) = 26
> Always start with end index

1   1   1   1   6   7   9
1st way with 9: (9 + 7) + (1 + 1) + (1) = 19
2nd way without 9: 9 + (7 + 6) + (1 + 1) = 24

1   6   7   9
1st way: (9 + 7) + 1 = 17
2nd way: 9 + (7 + 6) = 22
Time: O(sortN)
Space: O(sortN)
"""

from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        ans = 0
        cost.sort()
        n = len(cost)

        curr = 0
        for i in range(n):
            remainder = i % 3
            if remainder == 0:
                curr = cost[n - i - 1]
            elif remainder == 2:
                ans += curr
                curr = 0
            else:
                curr += cost[n - i - 1]
        
        if curr != 0:
            ans += curr

        return ans

sol = Solution()
sol.minimumCost([5]) # 5
sol.minimumCost([1,2,2,5,6,7,9]) # 24
sol.minimumCost([1,1,1,1,6,7,9]) # 19
sol.minimumCost([1,6,7,9]) # 17
sol.minimumCost([1,6,7,9]) # 17
sol.minimumCost([1,2,3]) # 5
sol.minimumCost([6,5,7,9,2,2]) # 23
sol.minimumCost([5,5]) # 10
