"""
Problem: https://leetcode.com/problems/largest-submatrix-with-rearrangements
Idea: Build a matrix containing max consecutive ones at each position for each column

0   0   1
1   1   2
2   0   3

For each row, sort consecutive ones. This is to make column with highest consecutive ones closer.

0   0   1
1   1   2
0   2   3

iterating row to find ans = max(ans, val * (n - row))

Time: O(MNlog(N))
Space: O(sortN)
"""

from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ans = 0
        m, n = len(matrix), len(matrix[0])

        for y in range(m):
            for x in range(n):
                if matrix[y][x]:
                    if y == 0:
                        matrix[y][x] = 1
                    else:
                        matrix[y][x] = matrix[y - 1][x] + 1

        for y in range(m):
            matrix[y].sort()

            for x in range(n):
                if not matrix[y][x]:
                    continue
                ans = max(ans, matrix[y][x] * (n - x))

        return ans

sol = Solution()
sol.largestSubmatrix([[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1],[0,1,1,0,1,1,1,1,0,1,1,0,0,1,0,1,1,1,1,0,1,1,1,1,1,1]]) # 34
sol.largestSubmatrix([[0,0,1],[1,1,1],[1,0,1]]) # 4
sol.largestSubmatrix([[1,0,1,0,1]]) # 3
sol.largestSubmatrix([[1,1,0],[1,0,1]]) # 2
