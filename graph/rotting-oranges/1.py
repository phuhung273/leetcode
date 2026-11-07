"""
Problem: https://leetcode.com/problems/rotting-oranges
Idea: Iterate once, when encoutering rotten, push queue of form (minute, (y, x))
During iteration, if there is fresh one without any neighbour, immediately return -1
Continuously pop queue, if any fresh adjacent, change it to rotten, push queue minute + 1


BFS ensure if it becomes rotten, the minute is always minimum

Edge cases: only fresh, only rotten, nothing => solve by counting total


Dry run:
q = [(0, (0, 0))]
q = [(1, (1, 0)), (1, (0, 1))]
q = [(1, (0, 1)), (2, (1, 1))]
Time:
Space:
"""

from collections import deque

ROTTEN = 2
FRESH = 1

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        height, width = len(grid), len(grid[0])
        totalFresh = 0
        q = deque()

        for y in range(height):
            for x in range(width):
                if grid[y][x] == FRESH:
                    totalFresh += 1
                elif grid[y][x] == ROTTEN:
                    q.append((0, (y, x)))

        if not totalFresh:
            return 0

        ans = -1
        while q:
            minute, (y, x) = q.popleft()
            ans = max(ans, minute)

            candidates = [
                (y + 1, x),
                (y - 1, x),
                (y, x + 1),
                (y, x - 1),
            ]

            for candidateY, candidateX in candidates:
                if (-1 < candidateY < height) and (-1 < candidateX < width) and grid[candidateY][candidateX] == FRESH:
                    grid[candidateY][candidateX] = ROTTEN
                    totalFresh -= 1
                    q.append((minute + 1, (candidateY, candidateX)))
        if totalFresh > 0:
            return -1
        return ans

sol = Solution()
sol.orangesRotting([[0,2]]) # -1
sol.orangesRotting([[0,1,1],[0,0,1],[0,0,2]]) # 3
sol.orangesRotting([[2,1,1],[0,0,1],[0,0,2]]) # 2
sol.orangesRotting([[1,0,0],[0,0,0],[0,0,2]]) # -1
sol.orangesRotting([[1,1,1],[0,1,1],[1,0,1]]) # -1
sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) # 4
sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) # -1
