"""
Problem: https://leetcode.com/problems/rotate-string
Idea:
For i from 0 to n - 1, do an inner for loop check
Time: O(N^2)
Space: O(1)
"""

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        n = len(s)
        for i in range(n):
            found = True
            for j in range(n):
                if goal[j] != s[(j + i) % n]:
                    found = False
                    break
            if found:
                return True

        return False

sol = Solution()
sol.rotateString(s = "abcde", goal = "cdeab") # T
sol.rotateString(s = "abcde", goal = "abced") # F
