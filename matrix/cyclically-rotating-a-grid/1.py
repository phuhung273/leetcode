"""
Problem: https://leetcode.com/problems/cyclically-rotating-a-grid
Idea:
Take 1 layer as an array, this is like shifting k steps to the left. Then put it back into matrix.
Time:
Space:
"""

from typing import List


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        numLayer = min(m, n) // 2

        for layer in range(numLayer):
            startY = startX = layer
            endY = m - layer - 1
            endX = n - layer - 1

            arr = findOutestLayerArr(grid, startY, endY, startX, endX)
            arr = cyclicShiftLeftArr(arr, k)
            assignOutestLayer(grid, arr, startY, endY, startX, endX)
        return grid

def cyclicShiftLeftArr(arr: List[int], k: int) -> List[int]:
    n = len(arr)
    if n == k:
        return arr

    ans = [0] * n
    for i in range(n):
        ans[i] = arr[(i + k) % n]
    return ans

def findOutestLayerArr(grid: List[List[int]], startY: int, endY: int, startX: int, endX: int) -> List[int]:
    arr = [0] * (endY - startY + endX - startX) * 2
    i = 0

    for x in range(startX, endX + 1):
        arr[i] = grid[startY][x]
        i += 1
    
    for y in range(startY + 1, endY):
        arr[i] = grid[y][endX]
        i += 1
    
    for x in range(endX, startX - 1, -1):
        arr[i] = grid[endY][x]
        i += 1

    for y in range(endY - 1, startY, -1):
        arr[i] = grid[y][startX]
        i += 1
    return arr

def assignOutestLayer(grid: List[List[int]], arr, startY: int, endY: int, startX: int, endX: int):
    i = 0

    for x in range(startX, endX + 1):
        grid[startY][x] = arr[i]
        i += 1
    
    for y in range(startY + 1, endY):
        grid[y][endX] = arr[i]
        i += 1
    
    for x in range(endX, startX - 1, -1):
        grid[endY][x] = arr[i]
        i += 1

    for y in range(endY - 1, startY, -1):
        grid[y][startX] = arr[i]
        i += 1

# cyclicShiftLeftArr([1,2,3], 2)
# findOutestLayerArr([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 0, 3, 0, 3)

sol = Solution()
sol.rotateGrid(grid = [[40,10],[30,20]], k = 1)
sol.rotateGrid(grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2)
