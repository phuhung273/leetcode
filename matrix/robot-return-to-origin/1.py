"""
Problem: https://leetcode.com/problems/robot-return-to-origin
Idea: Use 2 vertical and horizontal denoting how far robot have travelled
Up/Down: vertical +/- 1
Time: O(N)
Space: O(1)
"""

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        vertical = 0
        horizontal = 0

        for move in moves:
            if move == 'U':
                vertical += 1
            elif move == 'D':
                vertical -= 1
            elif move == 'L':
                horizontal -= 1
            else:
                horizontal += 1

        return horizontal == 0 and vertical == 0

sol = Solution()
sol.judgeCircle("UD")
sol.judgeCircle("LL")
