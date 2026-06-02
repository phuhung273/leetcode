"""
Problem: https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i
Idea: Brute force
Time: O(mn)
Space: O(1)
-------------------------------
Idea:
Land start 1st, find minimun of endLand > iterate water and find min(max(endLand, startWater) + waterDuration)
Do it again with water starts 1st
Time: O(m + n)
Space: O(1)
"""

import math
from typing import List


class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def solve(start1: List[int], duration1: List[int], start2: List[int], duration2: List[int]) -> int:
            end1 = math.inf
            for i in range(len(start1)):
                end1 = min(end1, start1[i] + duration1[i])
            ans = math.inf
            for i in range(len(start2)):
                ans = min(ans, max(end1, start2[i]) + duration2[i])
            return int(ans)

        return min(
            solve(landStartTime, landDuration, waterStartTime, waterDuration),
            solve(waterStartTime, waterDuration, landStartTime, landDuration),
        )

sol = Solution()
sol.earliestFinishTime(landStartTime = [2,8], landDuration = [4,1], waterStartTime = [6], waterDuration = [3]) # 9
sol.earliestFinishTime(landStartTime = [5], landDuration = [3], waterStartTime = [1], waterDuration = [10]) # 14
