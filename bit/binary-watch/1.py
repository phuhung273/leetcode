"""
Problem: https://leetcode.com/problems/binary-watch
Idea:
Hour: max 12 = 3 on
Minute: max 60 = 5 on

Precompute bit count of 0-59
Calculate all possible turnedOn bits for minute and hour.

Time:
Space: O(1) = 60
"""

from collections import defaultdict
from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn > 8:
            return []
        
        def bitCount(num: int):
            count = 0
            while num != 0:
                if num & 1 == 1:
                    count += 1
                num >>= 1
            return count
        
        bitCountMap = defaultdict(list)
        for i in range(60):
            count = bitCount(i)
            bitCountMap[count].append(i)
        
        ans = []
        
        for hour in range(turnedOn + 1):
            minute = turnedOn - hour
            if minute > 5 or hour > 3:
                continue
            for h in bitCountMap[hour]:
                if h > 11:
                    continue
                for m in bitCountMap[minute]:
                    if m < 10:
                        ans.append(f'{h}:0{m}')
                    else:
                        ans.append(f'{h}:{m}')

        return ans

sol = Solution()
sol.readBinaryWatch(4)
sol.readBinaryWatch(1)
sol.readBinaryWatch(9)
