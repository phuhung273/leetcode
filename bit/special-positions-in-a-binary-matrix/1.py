"""
Problem: https://leetcode.com/problems/special-positions-in-a-binary-matrix
Idea:
Iterate all the rows, record the first column of 1.
If there is another 1, continue to next row.
If not, check that column.
If column invalid, save column index to not check next time

Time: O(m*n)
Space: O(m+n)

---

Iterate to build 2 array rows/cols of size m/n denoting number of 1s for each row/cols
Iterate again, when found 1, check if rows and cols are also 1

Time: O(m * (m + n))
Space: O(n)
"""

from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans = 0
        m, n = len(mat), len(mat[0])
        rows = [0] * m
        cols = [0] * n

        for y in range(m):
            for x in range(n):
                if mat[y][x]:
                    rows[y] += 1
                    cols[x] += 1
        
        for y in range(m):
            if rows[y] != 1:
                continue
            for x in range(n):
                if cols[x] != 1:
                    continue
                if mat[y][x]:
                    ans += 1
                    break

        return ans

    # def numSpecial(self, mat: List[List[int]]) -> int:
    #     ans = 0
    #     invalidColumnSet = set()

    #     for y in range(len(mat)):
    #         firstValidColumn = -1
    #         isValid = True
    #         for x in range(len(mat[0])):
    #             if mat[y][x]:
    #                 if firstValidColumn == -1:
    #                     firstValidColumn = x
    #                 else:
    #                     isValid = False
    #                     break
    #         if firstValidColumn == -1 or not isValid or firstValidColumn in invalidColumnSet:
    #             continue

    #         isValid = True
    #         for j in range(len(mat)):
    #             if mat[j][firstValidColumn] and j != y:
    #                 invalidColumnSet.add(firstValidColumn)
    #                 isValid = False
    #                 break

    #         if isValid:
    #             ans += 1

    #     return ans

sol = Solution()
sol.numSpecial([[1,0,0],[0,0,1],[1,0,0]]) # 1
sol.numSpecial([[1,0,0],[0,1,0],[0,0,1]]) # 3
