"""
Problem: https://leetcode.com/problems/asteroid-collision
Idea: Use a stack
If same sign, push stack
While diff sign and abs more than head, pop
Time: O(N)
Space: O(N)
"""

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if not stack or asteroid > 0 or (stack[-1] < 0 and asteroid < 0):
                stack.append(asteroid)
                continue

            while stack and stack[-1] > 0 and -asteroid > stack[-1]:
                stack.pop()

            if stack and stack[-1] > 0 and -asteroid == stack[-1]:
                stack.pop()
            elif not stack or stack[-1] < 0:
                stack.append(asteroid)

        return stack

sol = Solution()
sol.asteroidCollision([-2,-1,1,-2])
sol.asteroidCollision([-2,-2,1,-2])
sol.asteroidCollision([5,10,-5])
sol.asteroidCollision([8,-8])
sol.asteroidCollision([10,2,-5])
sol.asteroidCollision([3,5,-6,2,-1,4])
