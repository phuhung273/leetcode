"""
Problem: https://leetcode.com/problems/count-the-number-of-special-characters-ii
Idea:
Time:
Space:
"""

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = set()
        special = set()
        notSpecial = set()

        for char in word:
            if char == char.lower():
                if char in special:
                    notSpecial.add(char)
                else:
                    lower.add(char)
            else:
                if char.lower() in lower:
                    special.add(char.lower())
                else:
                    notSpecial.add(char.lower())
        
        ans = 0
        for char in special:
            if char not in notSpecial:
                ans += 1
        return ans

sol = Solution()
sol.numberOfSpecialChars("AbcbDBdD") # 1
sol.numberOfSpecialChars("aaAbcBC") # 3
sol.numberOfSpecialChars("abc") # 0
sol.numberOfSpecialChars("AbBCab") # 0
