"""
Problem: https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid
Idea: For each row, calculate maxRight arr denoting index of right most 1
For each i, swap row i with closest row where maxRight <= i
Time: O(N^2)
Space: O(N)
"""

from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0
        maxRight = [-1] * n

        for y in range(n):
            for x in range(n - 1, -1, -1):
                if grid[y][x] == 1:
                    maxRight[y] = x
                    break

        for i in range(n):
            k = -1

            for j in range(i, n):
                if maxRight[j] <= i:
                    ans += j - i
                    k = j
                    break

            if k == -1:
                return -1

            for l in range(k, i, -1):
                maxRight[l], maxRight[l - 1] = maxRight[l - 1], maxRight[l]
        return ans

sol = Solution()
sol.minSwaps([[0,0],[0,1]]) # 0
sol.minSwaps([[0,0,1],[1,1,0],[1,0,0]]) # 3
sol.minSwaps([[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]) # -1
sol.minSwaps([[1,0,0],[1,1,0],[1,1,1]]) # 0
