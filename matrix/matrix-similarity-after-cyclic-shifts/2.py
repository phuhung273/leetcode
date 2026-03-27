"""
Problem: https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts
Idea: k %= n

Right shift is same as left shift because left cell move right and same as right cell move left
Iterate and check if x and x + k % n is the same

Time: O(mn)
Space: O(1)
"""

from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])

        if k %n == 0:
            return True

        for y in range(m):
            for x in range(n):
                if mat[y][x] != mat[y][(x + k) % n]:
                    return False

        return True

sol = Solution()
sol.areSimilar(mat = [[5,4,5,10,5]], k = 4) # F
sol.areSimilar(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 4) # F
sol.areSimilar(mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2) # T
sol.areSimilar(mat = [[2,2],[2,2]], k = 3) # T
