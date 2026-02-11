"""
Problem: https://leetcode.com/problems/longest-balanced-subarray-i

Idea:
Sliding window: doesn't work because not sure when to move left pointer

----

Prefix sum: build an evenCount arr where evenCount[i] tells how many even numbers are in subarray [0,i] inclusively
For every i,j, check if evenCount[j] - evenCount[i] = oddCount[j] - oddCount[i]

> evenCount[j] - evenCount[i] is incorrect: element after i is removed if it has a duplicate before i

----

Brute force
Time: O(N^2)
Space: O(N)
"""

from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            oddSet = set()
            evenSet = set()
            for j in range(i, len(nums)):
                if nums[j] % 2 == 0:
                    evenSet.add(nums[j])
                else:
                    oddSet.add(nums[j])
                if len(evenSet) == len(oddSet):
                    ans = max(ans, j - i + 1)

        return ans

sol = Solution()
sol.longestBalanced([2,5,4,3])
sol.longestBalanced([3,2,2,5,4])
sol.longestBalanced([1,2,3,2])
