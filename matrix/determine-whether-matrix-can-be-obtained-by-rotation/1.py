"""
Problem: https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation
Idea: Flip vertically then check a[y][x] = b[x][y]
Time: O(n^2)
Space: O(1)
"""

from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def check():
            for y in range(len(mat)):
                for x in range(len(mat[0])):
                    if mat[x][y] != target[x][y]:
                        return False
            return True

        def rotate():
            mat.reverse()

            for y in range(len(mat)):
                for x in range(y + 1, len(mat[0])):
                    mat[y][x], mat[x][y] = mat[x][y], mat[y][x]

        ans = False
        for _ in range(4):
            ans = check()
            if ans:
                break
            rotate()

        return ans
    
    

sol = Solution()
sol.findRotation(mat = [[0,0],[0,1]], target = [[0,0],[1,0]]) # T
sol.findRotation(mat = [[0,1],[1,0]], target = [[1,0],[0,1]]) # T
sol.findRotation(mat = [[0,1],[1,1]], target = [[1,0],[0,1]]) # F
sol.findRotation(mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]) # T
