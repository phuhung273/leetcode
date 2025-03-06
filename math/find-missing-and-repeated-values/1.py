from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        memo = {}
        result = []
        currSum = int(n**2 * (n**2 + 1) / 2)

        for y in range(n):
            for x in range(n):
                val = grid[y][x]

                if val in memo:
                    result.append(val)
                else:
                    currSum -= val

                memo[val] = True

        result.append(currSum)
        return result

sol = Solution()
sol.findMissingAndRepeatedValues([[1,3],[2,2]]) # [2,4]