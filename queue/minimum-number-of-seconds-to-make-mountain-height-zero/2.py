"""
Problem: https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero
Idea:
Binary search with validation: 
3 + 6 + 9 = 3*(1 + 2 + 3) = 3 * (n * (n + 1) / 2)
-> n^2 + n - 2 * mid / t = 0
delta = 1 + 8*mid / t
-> n = (-1 + sqrt(delta)) / 2

sum(n[i]) > h: go left

Time: log(max(N)*H)*N
Space:  O(1)
"""

import math
from typing import List



class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        lo, hi = 0, max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2

        while lo < hi:
            mid = lo + (hi - lo) // 2
            sumHeight = 0
            for t in workerTimes:
                sumHeight += (-1 + math.sqrt(1 + 8 * mid / t)) // 2

            if sumHeight >= mountainHeight:
                hi = mid
            else:
                lo = mid + 1
        return lo

sol = Solution()
sol.minNumberOfSeconds(mountainHeight = 100000, workerTimes = [1]) # 10
sol.minNumberOfSeconds(mountainHeight = 5, workerTimes = [1,7]) # 10
sol.minNumberOfSeconds(mountainHeight = 4, workerTimes = [2,1,1]) # 3
sol.minNumberOfSeconds(mountainHeight = 10, workerTimes = [3,2,2,4]) # 12
sol.minNumberOfSeconds(mountainHeight = 5, workerTimes = [1]) # 15
