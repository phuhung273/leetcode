"""
Problem: https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix
Idea: Brute force
Time: O(mnk)
Space:
"""

from typing import List


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        if k == 1:
            return [[0] * (n - k + 1) for _ in range(m - k + 1)]
        
        inf = 3 * 10**5

        ans = [[inf] * (n - k + 1) for _ in range(m - k + 1)]

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                arr = []
                for y in range(k):
                    for x in range(k):
                        arr.append(grid[i + y][j + x])

                arr.sort()
                val = inf
                for t in range(1, len(arr)):
                    if arr[t] == arr[t - 1]:
                        continue
                    val = min(val, abs(arr[t] - arr[t - 1]))
                if val == inf:
                    ans[i][j] = 0
                else:
                    ans[i][j] = val

        return ans

sol = Solution()
sol.minAbsDiff(grid = [[41792,59482],[49179,-22072]], k = 2) # [[2]]
# sol.minAbsDiff(grid = [[1,8],[3,-2]], k = 2) # [[2]]
# sol.minAbsDiff(grid = [[1,8,1],[3,-2, 1]], k = 2) # [[2,0]]
sol.minAbsDiff(grid = [[3,-1]], k = 1) # [[0,0]]
sol.minAbsDiff(grid = [[1,-2,3],[2,3,5]], k = 2) # [[1,2]]
