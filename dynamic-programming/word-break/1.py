"""
Problem: https://leetcode.com/problems/word-break
Idea: DP
Time: O(L^2*N + M * L) with N is string length, L is max length of dict, M is dict capacity
Space: O(M)
"""

from functools import cache
from typing import List


class Solution:
    # Top down
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        maxLen = max(len(w) for w in wordDict) # O(M * L)

        @cache
        def dp(i: int) -> bool:
            if i == len(s):
                return True

            for j in range(i, min(i + maxLen + 1, len(s) + 1)): # O(L)
                word = s[i:j] # O(L)
                if word in wordSet and dp(j):
                    return True
            return False

        return dp(0)

sol = Solution()
sol.wordBreak(s = "leetcode", wordDict = ["leet","code"])
sol.wordBreak(s = "applepenapple", wordDict = ["apple","pen"])
sol.wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"])
