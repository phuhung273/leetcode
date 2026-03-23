"""
Problem: https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix
Idea:

DP
dp[y][0] = dp[y - 1][0] * grid[y][0]
dp[0][x] = dp[0][x - 1] * dp[0][x]
dp[y][x] = max(dp[y - 1][x], dp[y][x - 1]) * grid[y][x]
> wrong as max might eliminate negative which multiplying with other negative to produce the high positive

---

Find highest and lowest

Time: O(mn)
Space: O(n)
"""

from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dpHigh = [0] * n
        dpLow = [0] * n

        dpHigh[0] = dpLow[0] = grid[0][0]

        for x in range(1, n):
            dpHigh[x] = dpLow[x] = dpHigh[x - 1] * grid[0][x]
        
        for y in range(1, m):
            for x in range(n):
                if x == 0:
                    dpHigh[0] = dpLow[0] = dpHigh[0] * grid[y][0]
                    continue

                high = max(
                    dpHigh[x] * grid[y][x],
                    dpHigh[x - 1] * grid[y][x],
                    dpLow[x] * grid[y][x],
                    dpLow[x - 1] * grid[y][x],
                )
                low = min(
                    dpHigh[x] * grid[y][x],
                    dpHigh[x - 1] * grid[y][x],
                    dpLow[x] * grid[y][x],
                    dpLow[x - 1] * grid[y][x],
                )

                dpHigh[x] = high
                dpLow[x] = low

        ans = dpHigh[n - 1] % (10**9 + 7) if dpHigh[n - 1] >= 0 else -1
        return ans

sol = Solution()
sol.maxProductPath([[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]) # -1
sol.maxProductPath([[1,-2,1],[1,-2,1],[3,-4,1]]) # 8
sol.maxProductPath([[1,3],[0,-4]]) # 0
