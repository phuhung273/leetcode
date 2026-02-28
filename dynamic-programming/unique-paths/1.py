"""
Problem: https://leetcode.com/problems/unique-paths
Idea: DP 2D, dp[m][n] = dp[m - 1][n] + dp[m][n - 1]
Time: O(m * n)
Space: O(n)
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * n
        
        for y in range(m):
            for x in range(n):
                if y == 0 or x == 0:
                    dp[x] = 1
                    continue

                dp[x] += dp[x - 1]
        return dp[n - 1]

sol = Solution()
sol.uniquePaths(3, 7) # 28
sol.uniquePaths(3, 2) # 3
