"""
Problem: https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts
Idea: k %= n

Double each row.
For even, left = 0, right = k. Iterate and check
For odd, left = 0, right = n - k. Do the same

Time: O(mn)
Space: O(mn)

--------------

For even row after k shift left:
If i < n - k, compare i and i + k. Else, compare i and i + k - n
Iterate and check if all before and after are the same

For odd row after k shift right:
If i < k, compare i and n - k + i

Time: O(mn)
Space: O(1)
"""

from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        k %= n

        if k == 0:
            return True

        for y in range(m):
            for x in range(n):
                if y % 2 == 0:
                    if x < n - k and mat[y][x] != mat[y][x + k]:
                        return False
                    elif x >= n - k and mat[y][x] != mat[y][x + k - n]:
                        return False
                else:
                    if x < k and mat[y][x] != mat[y][n - k + x]:
                        return False
                    elif x >= k and mat[y][x] != mat[y][x + k - n]:
                        return False

        return True

sol = Solution()
sol.areSimilar(mat = [[5,4,5,10,5]], k = 4) # F
sol.areSimilar(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 4) # F
sol.areSimilar(mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2) # T
sol.areSimilar(mat = [[2,2],[2,2]], k = 3) # T
