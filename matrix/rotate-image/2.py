"""
Problem: https://leetcode.com/problems/rotate-image
Idea: Reverse and swap m[y][x] with m[x][y]

5   1   9   11
2   4   8   10
13  3   6   7
15  14  12  16

15  14  12  16
13  3   6   7
2   4   8   10
5   1   9   11

Time: O(N^2)
Space: O(1)
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        n = len(matrix)

        for y in range(n):
            for x in range(y, n):
                matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]
        return

sol = Solution()
sol.rotate([[1,2,3],[4,5,6],[7,8,9]]) # [[7,4,1],[8,5,2],[9,6,3]]
sol.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]) # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
