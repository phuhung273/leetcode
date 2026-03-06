"""
Problem: https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones
Idea: have a boolean isEnded
Time: O(N)
Space: O(1)
"""

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        isEnded = False
        for char in s:
            if char == '0':
                isEnded = True
            if char == '1' and isEnded:
                return False
        return True

sol = Solution()
sol.checkOnesSegment("1001") # F
sol.checkOnesSegment("110") # T
