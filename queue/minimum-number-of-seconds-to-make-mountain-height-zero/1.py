"""
Problem: https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero
Idea:
Initially, put all in a min queue of (time, worker[i])
Pop queue and sum
Custom comparator: if same time, choose woker with current lowest time
Time: O(hlogN) with h is height
Space: O(N)
"""

import heapq
from typing import List



class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        ans = 0
        q = []
        for i in range(len(workerTimes)):
            heapq.heappush(q, (workerTimes[i], (i, 1)))

        for _ in range(mountainHeight):
            t, (i, count) = heapq.heappop(q)
            ans = max(ans, t)
            count += 1
            heapq.heappush(q, (t + workerTimes[i] * count, (i, count)))
        return ans

sol = Solution()
sol.minNumberOfSeconds(mountainHeight = 5, workerTimes = [1,7]) # 10
sol.minNumberOfSeconds(mountainHeight = 4, workerTimes = [2,1,1]) # 3
sol.minNumberOfSeconds(mountainHeight = 10, workerTimes = [3,2,2,4]) # 12
sol.minNumberOfSeconds(mountainHeight = 5, workerTimes = [1]) # 15
