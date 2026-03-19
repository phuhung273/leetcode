"""
Problem: https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y
Idea: contain mean contain the value of grid[0][0] of contain top left

Contain top left:
Have an arr cols where cols[i] contain count of (X, Y) of that column
Iterate all rows, build a prefixCount and check

Time: O(MN)
Space: O(N)
"""

from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        colXs = [0] * n
        colYs = [0] * n

        for i in range(m):
            prefixCountX = 0
            prefixCountY = 0

            for j in range(n):
                if grid[i][j] == 'X':
                    prefixCountX += 1
                elif grid[i][j] == 'Y':
                    prefixCountY += 1

                colXs[j] += prefixCountX
                colYs[j] += prefixCountY

                if colXs[j] == colYs[j] and colXs[j] > 0:
                    ans += 1

        return ans

sol = Solution()
sol.numberOfSubmatrices([["Y","."],["X","."]]) # 2
sol.numberOfSubmatrices([["X","Y","."],["Y",".","."]]) # 3
sol.numberOfSubmatrices([["X","X"],["X","Y"]]) # 0
sol.numberOfSubmatrices([[".","."],[".","."]]) # 0
