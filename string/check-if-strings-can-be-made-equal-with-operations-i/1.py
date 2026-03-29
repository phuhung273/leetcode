"""
Problem: https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i
Idea: Iterate, if different, check is swapping correct
Time: O(1)
Space: O(1)
"""

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        skip = 0

        for i in range(4):
            if (skip >> i) & 1:
                continue
            if s1[i] != s2[i]:
                if i > 1:
                    return False
                if s1[i + 2] != s2[i] or s1[i] != s2[i + 2]:
                    return False
                skip |= 1 << (i + 2)
        return True

sol = Solution()
sol.canBeEqual(s1 = "abcd", s2 = "cdab") # T
sol.canBeEqual(s1 = "jegy", s2 = "jeyg") # T
sol.canBeEqual(s1 = "abcd", s2 = "dacb") # F
