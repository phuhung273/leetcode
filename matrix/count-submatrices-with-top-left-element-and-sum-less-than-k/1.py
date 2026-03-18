"""
Problem: https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k
Idea:
Iterate all rows. If up == -1, break
Elif cell = left + up > k, fill with -1, break
Else: ans += 1, fill cell = ans

Time: O(MN)
Space: O(1)
"""

from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        if grid[0][0] > k:
            return 0

        ans = 0
        m, n = len(grid), len(grid[0])

        for y in range(m):
            prefixSum = 0
            for x in range(n):
                if y > 0 and grid[y - 1][x] == -1:
                    grid[y][x] = -1
                    break

                prefixSum += grid[y][x]
                val = prefixSum
                if y > 0:
                    val += grid[y - 1][x]

                if val > k:
                    grid[y][x] = -1
                    break
                else:
                    ans += 1
                    grid[y][x] = val
        return ans

sol = Solution()
sol.countSubmatrices(grid = [[9,10,5],[4,5,10],[1,5,3]], k = 14) # 3
sol.countSubmatrices(grid = [[7,7,10,9],[10,5,10,3]], k = 54) # 7
sol.countSubmatrices(grid = [[7,6,3],[6,6,1]], k = 8) # 1
sol.countSubmatrices(grid = [[7,6,3],[6,6,1]], k = 18) # 4
sol.countSubmatrices(grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20) # 6
