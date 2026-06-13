"""
Problem: https://leetcode.com/problems/weighted-word-mapping
Idea:
Time:
Space:
"""

from typing import List


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = ''

        for word in words:
            weight = 0
            for char in word:
                weight += weights[ord(char) - ord('a')]
            ans += chr(25 - (weight % 26) + ord('a'))
        return ans

sol = Solution()
sol.mapWordWeights(words = ["abcd","def","xyz"], weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]) # rij
sol.mapWordWeights(words = ["a","b","c"], weights = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) # yyy
sol.mapWordWeights(words = ["abcd"], weights = [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5]) # g
