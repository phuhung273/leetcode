"""
Problem: https://leetcode.com/problems/maximum-size-subarray-sum-equals-k
Idea: Build a prefixSumMap
Time: O(N)
Space: O(N)
"""

from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefixSumMap = { 0: -1 }
        prefixSum = 0
        ans = 0
        for i, num in enumerate(nums):
            prefixSum += num

            if prefixSum not in prefixSumMap:
                prefixSumMap[prefixSum] = i

            if prefixSum - k in prefixSumMap:
                ans = max(ans, i - prefixSumMap[prefixSum - k])
        
        return ans

sol = Solution()
sol.maxSubArrayLen(nums = [1,-1,5,-2,3], k = 3)
sol.maxSubArrayLen(nums = [-2,-1,2,1], k = 1)
