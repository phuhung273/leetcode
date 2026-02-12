"""
Problem: https://leetcode.com/problems/longest-balanced-substring-i
Idea:
Brute force: save a counter
Time: O(N^2)
Space: O(N)
"""

from typing import Counter


class Solution:
    def longestBalanced(self, s: str) -> int:
        ans = 1
        for i in range(len(s)):
            counter = Counter()
            for j in range(i, len(s)):
                counter[s[j]] += 1
                count = counter[s[i]]
                isValid = True
                for char in counter:
                    if counter[char] != count:
                        isValid = False
                        break
                if isValid:
                    ans = max(ans, j - i + 1)
        return ans

sol = Solution()
sol.longestBalanced("kl")
sol.longestBalanced("abbac")
sol.longestBalanced("zzabccy")
sol.longestBalanced("aba")
