"""
Problem: https://leetcode.com/problems/longest-increasing-subsequence

Idea: Keep a subsequence
For every item, bisect left. If pos >= len, append, else replace

Time: O(NlogN)
Space: O(N)
"""

from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence = []
        ans = 0
        for num in nums:
            pos = bisect_left(subsequence, num)
            if pos >= len(subsequence):
                subsequence.append(num)
            else:
                subsequence[pos] = num
            ans = max(ans, len(subsequence))
        return ans

sol = Solution()
sol.lengthOfLIS([10,9,2,5,3,7,101,18]) # 4
sol.lengthOfLIS([0,1,0,3,2,3]) # 4
sol.lengthOfLIS([7,7,7,7,7,7,7]) # 1
