"""
Problem: https://leetcode.com/problems/counting-bits
Idea:
f(1111) = f(111) + 1
f(x) = f(x - count) + 1
count +=1 when x == 2**count 
Time: O(N)
Space: O(1)
"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        milestone = 1
        nextMilestone = 2
        for i in range(1, n + 1):
            if i == nextMilestone:
                milestone <<= 1
                nextMilestone <<= 1
            ans[i] = ans[i - milestone] + 1
        return ans

sol = Solution()
sol.countBits(2) # [0,1,1]
sol.countBits(5) # [0,1,1,2,1,2]
