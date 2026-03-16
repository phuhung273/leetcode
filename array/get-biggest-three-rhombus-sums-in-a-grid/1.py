"""
Problem: https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid
Idea:
Start with rhombus of size 0 to (if n odd then math.ceil(n/2) + 1 else n / 2). Iterate to find max
Time: O(n^4)
Space: O(1)
"""

import heapq
from typing import List


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        ans = []
        m = len(grid)
        n = len(grid[0])
        minMn = min(m, n)
        maxSize = minMn // 2 if minMn % 2 == 0 else minMn // 2 + 1

        def handleMax(rhombusSum: int):
            if rhombusSum in ans:
                return

            heapq.heappush(ans, rhombusSum)
            if len(ans) > 3:
                heapq.heappop(ans)

        for size in range(maxSize):
            for y in range(m - 2 * size):
                for x in range(size, n - size):
                    curr = 0
                    centerY = y + size
                    curr += grid[centerY + size][x]
                    if size != 0:
                        curr += grid[centerY - size][x] + grid[centerY][x - size] + grid[centerY][x + size]

                    for i in range(1, size):
                        curr += grid[centerY - i][x + size - i] \
                            + grid[centerY + i][x + size - i] \
                            + grid[centerY - i][x - size + i] \
                            + grid[centerY + i][x - size + i]
                    
                    handleMax(curr)

        ans.sort(reverse=True)
        return ans

sol = Solution()
sol.getBiggestThree([[15,14,15,19,6,18,15,14],[18,7,8,10,3,5,11,19],[20,11,10,1,6,3,16,3],[7,14,4,9,18,14,13,3],[20,5,15,3,9,8,16,16],[6,7,4,12,2,19,11,20],[20,11,10,3,4,9,5,15],[13,10,4,18,16,2,4,20]]) # [148,130,96]
sol.getBiggestThree([[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]) # [228,216,211]
sol.getBiggestThree([[1,2,3],[4,5,6],[7,8,9]]) # [20,9,8]
sol.getBiggestThree([[7,7,7]]) # 7
