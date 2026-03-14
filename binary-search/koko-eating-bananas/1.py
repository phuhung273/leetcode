"""
Problem: https://leetcode.com/problems/koko-eating-bananas
Idea: Binary search, lo = 0, hi = 2^32 - 1

k = 4
[3,6,7,11]
[0,6,7,11]
[0,2,7,11]
[0,0,7,11]
[0,0,3,11]
[0,0,0,11]
[0,0,0,7]
[0,0,0,3]
[0,0,0,0]

k = 3
[3,6,7,11]
[0,6,7,11]
[0,3,7,11]
[0,0,7,11]
[0,0,4,11]
[0,0,1,11]
[0,0,0,11]
[0,0,0,8]
[0,0,0,5]
[0,0,0,2]
[0,0,0,0]

Decision: sum(math.ceil(piles[i] / k)) > h --> go right

Time: O(Nlog(constant)) = O(N)
Space: O(1)
"""

import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 0, 10**9
        mid = 0

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid == 0:
                break

            time = 0
            for p in piles:
                time += math.ceil(p / mid)
            if time > h:
                lo = mid + 1
            else:
                hi = mid

        if mid == 0:
            return 1
        return lo

sol = Solution()
sol.minEatingSpeed(piles = [312884470], h = 968709470) # 4
sol.minEatingSpeed(piles = [3,6,7,11], h = 8) # 4
sol.minEatingSpeed(piles = [30,11,23,4,20], h = 5) # 30
sol.minEatingSpeed(piles = [30,11,23,4,20], h = 6) # 23
