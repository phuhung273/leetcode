"""
Problem: https://leetcode.com/problems/destroying-asteroids
Idea: sort ascending and destroy all
Time: O(sortN)
Space: O(sortN)
"""

from typing import List


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        for weight in asteroids:
            if mass < weight:
                return False
            mass += weight

            if mass >= asteroids[-1]:
                return True

        return True

sol = Solution()
sol.asteroidsDestroyed(mass = 10, asteroids = [3,9,19,5,21]) # T
sol.asteroidsDestroyed(mass = 5, asteroids = [4,9,23,4]) # F
