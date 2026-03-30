"""
Problem: https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii
Idea:

a   b   c   d   b   a
c   a   b   d   a   b

Even(a, c, b), Odd(b, d, a) > b,a,d > a,b,d > a,d,b > 
Even(c, b, a), Odd(a, d, b)

> The problem can be broken down into Check Even, then check Odd

> With infinite swap, can we make any permutation ? Yes > Count char


Time: O(N)
Space: O(N)
"""

from typing import Counter


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)
        evenCounter = Counter()
        oddCounter = Counter()

        for i in range(n):
            if i % 2:
                oddCounter[s1[i]] += 1
                oddCounter[s2[i]] -= 1
            else:
                evenCounter[s1[i]] += 1
                evenCounter[s2[i]] -= 1

        for key in evenCounter:
            if evenCounter[key] < 0:
                return False
        for key in oddCounter:
            if oddCounter[key] < 0:
                return False

        return True

sol = Solution()
sol.checkStrings(s1 = "abcdba", s2 = "cabdab") # T
sol.checkStrings(s1 = "abe", s2 = "bea") # F
