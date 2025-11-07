"""
Time: O(N^k)
Space: O(N^k) = N^k(ans) + k(current) + k(depth of recursion stack) * 1(input i)
"""

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        current = []

        def choose(i: int):
            if len(current) == k:
                ans.append(current.copy())
                return

            for j in range(i, n + 1):
                current.append(j)
                choose(j + 1)
                current.pop()

        choose(1)
        return ans

sol = Solution()
sol.combine(n=4, k=2)
sol.combine(n=1, k=1)
