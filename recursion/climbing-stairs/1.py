"""
Time: O(N) since we have cache => calculate once for every n
Space: O(N) = N(depth of recursion stack) * 1(input var k) + N(cache)
"""

from functools import cache


class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def climb(k: int) -> int:
            if k in [1,2]:
                return 1
            return climb(k - 1) + climb(k - 2)
        return climb(n + 1)

sol = Solution()
ans = sol.climbStairs(2)
ans = sol.climbStairs(3)
print('test')
