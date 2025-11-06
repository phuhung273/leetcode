"""
Time: O(4^N) = N digits, each with max 4 options
Space: O(N) = N (depth of recursion stack) * 1 (input var i)
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        charMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        result = []
        current = []

        def choose(i: int):
            if i == len(digits):
                result.append("".join(current))
                return

            for j in charMap[digits[i]]:
                current.append(j)
                choose(i + 1)
                current.pop()
        choose(0)
        return result

sol = Solution()
# sol.letterCombinations('23')
sol.letterCombinations('2')
