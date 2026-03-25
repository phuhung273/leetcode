"""
Problem: https://leetcode.com/problems/equal-sum-grid-partition-i
Idea: Save sum of rows and cols to a set, check if total / 2 in set
Time: O(mn)
Space: O(max(m,n))
"""

from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = 0
        vals = set()

        for y in range(m):
            if y > 0:
                vals.add(total)
            for x in range(n):
                total += grid[y][x]

        if total % 2 == 1:
            return False
        elif total // 2 in vals:
            return True
        
        total = 0
        vals = set()
        
        for x in range(n):
            if x > 0:
                vals.add(total)
            for y in range(m):
                total += grid[y][x]
        if total % 2 == 1:
            return False
        elif total // 2 in vals:
            return True

        return False

    # def canPartitionGrid(self, grid: List[List[int]]) -> bool:
    #     m, n = len(grid), len(grid[0])
    #     total = 0
    #     vals = set()
    #     prefixCols = [0] * n

    #     for y in range(m):
    #         if y > 0:
    #             vals.add(total)
    #         for x in range(n):
    #             total += grid[y][x]
    #             prefixCols[x] += grid[y][x]

    #             if y == m - 1:
    #                 if x > 0:
    #                     prefixCols[x] += prefixCols[x - 1]
    #                 vals.add(prefixCols[x])

    #     if total % 2 == 1:
    #         return False
        
    #     if total // 2 in vals:
    #         return True

    #     return False

sol = Solution()
sol.canPartitionGrid([[50042,40024,57692,14283],[35063,100000,100000,53154]]) # T
# sol.canPartitionGrid([[3, 3, 2]]) # F
# sol.canPartitionGrid([[49435,34517]]) # F
sol.canPartitionGrid([[1,4],[2,3]]) # T
sol.canPartitionGrid([[1,3],[2,4]]) # F
