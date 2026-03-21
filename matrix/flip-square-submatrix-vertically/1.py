"""
Problem: https://leetcode.com/problems/flip-square-submatrix-vertically
Idea:
If k is odd, up = x + k//2 - 1, down = up + 2
Else: up = x + k//2 - 1, down = up + 1
Iterate and swap
Time: O(k^2)
Space: O(1)
"""

from typing import List


class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        up = x + k // 2 - 1
        down = up + 1
        if k % 2 == 1:
            down += 1
        
        while up >= x:
            for col in range(y, y + k):
                grid[up][col], grid[down][col] = grid[down][col], grid[up][col]
            up -= 1
            down += 1
        return grid

sol = Solution()
sol.reverseSubmatrix(grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], x = 1, y = 0, k = 3)
sol.reverseSubmatrix(grid = [[3,4,2,3],[2,3,4,2]], x = 0, y = 2, k = 2)
