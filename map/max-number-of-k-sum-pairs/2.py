"""
Problem: https://leetcode.com/problems/max-number-of-k-sum-pairs/

Idea: Save in map. If found target - k > remove
Time: O(N)
Space: O(N)
"""

from typing import Counter, List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter()
        ans = 0
        for num in nums:
            if counter[k - num] > 0:
                ans += 1
                counter[k - num] -= 1
            else:
                counter[num] += 1
        return ans

sol = Solution()
sol.maxOperations(nums = [2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2], k = 3)
sol.maxOperations(nums = [1,2,3,4], k = 5)
sol.maxOperations(nums = [3,1,3,4,3], k = 6)
