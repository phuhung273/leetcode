"""
Problem: https://leetcode.com/problems/check-if-array-is-good
Idea: Have a hash set. Iterate and check if num is from [1,n]
Also have a bool foundN
Time: O(N)
Space: O(N)
"""

from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        countN = 0
        existSet = set()

        for num in nums:
            if num == n:
                countN += 1
                if countN > 2:
                    return False
            elif num <= 0 or num > n:
                return False
            else:
                if num in existSet:
                    return False
                existSet.add(num)

        return len(existSet) == n - 1

sol = Solution()
sol.isGood([2, 1, 4]) # False
sol.isGood([2, 1, 3]) # False
sol.isGood([2, 1, 3, 3, 3]) # False
sol.isGood([2, 1, 4, 4, 4]) # False
sol.isGood([1, 3, 3, 2]) # T
sol.isGood([1, 1]) # T
sol.isGood([3, 4, 4, 1, 2, 1]) # F
