"""
Problem: https://leetcode.com/problems/count-the-number-of-special-characters-i
"""

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = set()
        upper = set()
        special = set()

        for char in word:
            if char == char.lower():
                lower.add(char)

                if char.upper() in upper:
                    special.add(char.lower())
            else:
                upper.add(char)

                if char.lower() in lower:
                    special.add(char.lower())
        return len(special)

sol = Solution()
sol.numberOfSpecialChars("aaAbcBC")
sol.numberOfSpecialChars("abc")
sol.numberOfSpecialChars("abBCab")
