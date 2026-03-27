"""
Problem: https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts
Idea: k %= n

Double each row.
For even, left = 0, right = k. Iterate and check
For odd, left = 0, right = n - k. Do the same

--------------

For even row after k shift left:
If i < k, i become n - k + i. Else, i become i - k
Iterate and check if all before and after are the same

For odd row after k shift right:
If i < n - k, i become i + k. Else i become k - n + i

Time: O(mn)
Space: O(mn)
"""

from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        k %= n

        if k == 0:
            return True

        for y in range(m):
            left = 0
            right = 0
            if y % 2 == 0:
                right = k
            else:
                right = n - k

            mat[y].extend(mat[y])

            while left < n:
                if mat[y][left] != mat[y][right]:
                    return False
                left += 1
                right += 1
                
        return True

sol = Solution()
# sol.areSimilar(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 4) # F
sol.areSimilar(mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2) # T
sol.areSimilar(mat = [[2,2],[2,2]], k = 3) # T
