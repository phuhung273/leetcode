"""
Problem: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
Idea: Hash
a = 1
b = 2
c = 4
d = 8
Time: O(m + n)
Space: O(1)
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pHash = 0
        tHash = 0
        m = len(haystack)
        n = len(needle)
        prime = 10**9 + 7

        if m < n:
            return -1

        def hash(char: str):
            return (1 << (ord(char) - ord('a'))) % prime

        for i in range(n):
            pHash += hash(needle[i])
            tHash += hash(haystack[i])

        for i in range(m - n):
            if pHash == tHash and haystack[i: n + i] == needle:
                return i
            tHash += hash(haystack[n + i]) - hash(haystack[i])

        if pHash == tHash and haystack[m - n:] == needle:
            return m - n

        return -1

sol = Solution()
sol.strStr(haystack = "hello", needle = "ll")
sol.strStr(haystack = "sadbutsad", needle = "sad")
sol.strStr(haystack = "leetcode", needle = "leeto")
sol.strStr(haystack = "butsad", needle = "sad")
