"""
Problem: https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k
Idea: Save an array cols[i] storing sums of ith column so far
Time: O(MN)
Space: O(N)
"""

from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        if grid[0][0] > k:
            return 0

        ans = 0
        m, n = len(grid), len(grid[0])
        cols = [0] * n

        for y in range(m):
            prefixSum = 0
            for x in range(n):
                if cols[x] == -1:
                    break

                prefixSum += grid[y][x]
                cols[x] += prefixSum
                if cols[x] <= k:
                    ans += 1
                else:
                    cols[x] = -1
                    break
        return ans

sol = Solution()
sol.countSubmatrices(grid = [[9,10,5],[4,5,10],[1,5,3]], k = 14) # 3
sol.countSubmatrices(grid = [[7,7,10,9],[10,5,10,3]], k = 54) # 7
sol.countSubmatrices(grid = [[7,6,3],[6,6,1]], k = 8) # 1
sol.countSubmatrices(grid = [[7,6,3],[6,6,1]], k = 18) # 4
sol.countSubmatrices(grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20) # 6
