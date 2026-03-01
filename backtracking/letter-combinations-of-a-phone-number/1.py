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

        ans = []
        curr = []

        def choose(i: int):
            if i == len(digits):
                ans.append("".join(curr))
                return
            
            for char in charMap[digits[i]]:
                curr.append(char)
                choose(i + 1)
                curr.pop()

        choose(0)
        return ans

sol = Solution()
sol.letterCombinations('23')
sol.letterCombinations('2')
