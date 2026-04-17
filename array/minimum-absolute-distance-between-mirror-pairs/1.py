"""
Problem: https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs
Idea: Iterate and add its reverse to a map. Key: reverse, Val: index
Also save its reverse to prevent recalculation
Time: O(Nlog(M)) where M is max of nums
Space: O(N)
"""

import math
from typing import List


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        ans = math.inf
        reverseMap = {}
        reverseIndex = {}

        def reverse(num: int):
            result = 0
            while num != 0:
                result *= 10
                result += num % 10
                num //= 10
            return result
        
        for i, num in enumerate(nums):
            if num in reverseIndex:
                ans = min(ans, abs(i - reverseIndex[num]))
            
            rev = None
            if num in reverseMap:
                rev = reverseMap[num]
            else:
                rev = reverse(num)
                reverseMap[num] = rev
            reverseIndex[rev] = i

        return ans if ans != math.inf else -1 # type: ignore

sol = Solution()
sol.minMirrorPairDistance([12,21,45,33,54]) # 1
sol.minMirrorPairDistance([120,21]) # 1
sol.minMirrorPairDistance([21,120]) # -1
