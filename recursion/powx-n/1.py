"""
Problem: https://leetcode.com/problems/powx-n

Idea:
6^2 = 6^1 * 6^1
6^3 = 6^1 * 6^1 * 6
6^5 = 6^2 * 6^2 * 6
=> F(n) = F(n//2)^2 if n % 2 = 0, else F(n//2)^2 * x

For negative: F(n) = 1/F(-n)

Time: O(logN)

Space: O(logN)
"""

from functools import cache


class Solution:
    def myPow(self, x: float, n: int) -> float:
        @cache
        def F(n: int) -> float:
            if n == 0:
                return 1
            elif n == 1:
                return x

            half = F(n // 2)
            if n % 2 == 1:
                return half * half * x
            return half * half
        return F(n) if n >= 0 else 1/F(-n)

sol = Solution()
ans = sol.myPow(x = 2.00000, n = 10)
ans = sol.myPow(x = 2.10000, n = 3)
ans = sol.myPow(x = 2.00000, n = -2)
print('done')
