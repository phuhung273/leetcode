"""
Idea: Recursion

Get result of f(n-1)

Calculate row[n] from row[n-1]

Time: O(N^2) = 1 + 2 + 3 + ... + n

Space: O(N^3) = height of Recursion stack N * nums of local variable (numRows 1 + result N^2)
"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        result = self.generate(numRows - 1)
        newRow = [1]
        lastRow = result[len(result) - 1]
        for i in range(1, len(lastRow)):
            newRow.append(lastRow[i - 1] + lastRow[i])
        newRow.append(1)
        result.append(newRow)
        return result

sol = Solution()
sol.generate(5)
