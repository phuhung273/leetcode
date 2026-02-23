"""
Problem: https://leetcode.com/problems/n-th-tribonacci-number
Idea: bottom up DP
Time: O(N)
Space: O(1)
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1

        ans = 0
        prev0 = 0
        prev1 = 1
        prev2 = 1

        for _ in range(3, n + 1):
            ans = prev0 + prev1 + prev2
            prev0 = prev1
            prev1 = prev2
            prev2 = ans
        return ans

sol = Solution()
sol.tribonacci(4)
sol.tribonacci(25)
