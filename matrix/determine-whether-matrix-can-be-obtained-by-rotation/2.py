"""
Problem: https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation
Idea: 
Check current, flip 180 same with target
Rotate 90, redo step 1 
Time: O(n^2)
Space: O(1)
"""

from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        m, n = len(mat), len(mat[0])

        def check():
            for y in range(m):
                for x in range(n):
                    if mat[y][x] != target[y][x]:
                        return False
            return True

        def checkFlip180():
            for y in range(m):
                for x in range(n):
                    if mat[y][x] != target[m - 1 - y][n - 1 - x]:
                        return False
            return True
        
        def rotate():
            mat.reverse()

            for y in range(m):
                for x in range(y + 1, n):
                    mat[y][x], mat[x][y] = mat[x][y], mat[y][x]
        
        ans = check()
        if ans:
            return True
        ans = checkFlip180()
        if ans:
            return True
        
        rotate()
        ans = check()
        if ans:
            return True
        ans = checkFlip180()
        if ans:
            return True
        return False
    

sol = Solution()
sol.findRotation(mat = [[0,0],[0,1]], target = [[0,0],[1,0]]) # T
sol.findRotation(mat = [[0,1],[1,0]], target = [[1,0],[0,1]]) # T
sol.findRotation(mat = [[0,1],[1,1]], target = [[1,0],[0,1]]) # F
sol.findRotation(mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]) # T
