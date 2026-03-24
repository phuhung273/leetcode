"""
Problem: https://leetcode.com/problems/construct-product-matrix
Idea:
Brute force:
Iterate entire matrix to find product of all except for 0. Also track number of zeros. If numZeros > 1, stop early.
If numZeros > 1, all is 0
If numZeros = 1, all is 0 except for 0 element
Time: O(mn)
Space: O(1)

------------------------------------------------------

As product might be huge, slowing down calculation, we can use prefix and suffix calculation
"""

from typing import List


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        product = 1
        mod = 12345
        prefix = [[1] * n for _ in range(m)]

        for y in range(m):
            for x in range(n):
                prefix[y][x] = product
                product *= grid[y][x]
                product %= mod

        product = 1
        for y in range(m - 1, -1, -1):
            for x in range(n - 1, -1, -1):
                val = grid[y][x]
                grid[y][x] = (product * prefix[y][x]) % mod
                product = (product * val) % mod
        return grid

sol = Solution()
sol.constructProductMatrix([[1,2],[3,4]])
sol.constructProductMatrix([[12345],[2],[1]])
