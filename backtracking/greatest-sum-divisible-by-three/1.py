"""
Problem: https://leetcode.com/problems/greatest-sum-divisible-by-three

Idea: Backtrack and compare
=> Time exceed

If remainder: 0, currSum +=
1, currSum1 +=
If currSum1 % 3 == 0, currSum += currSum1, currSum1 = 0
currSum2 same for currSum1

=> Issue, largest 1 is at the end > sort descending > O(sort(N))

Time: O(N)
Space: O(1)
"""

from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        ans = 0
        currSum = 0

        def choose(i):
            nonlocal ans
            nonlocal currSum

            if i >= len(nums):
                return

            for j in range(i, len(nums)):
                currSum += nums[j]
                if currSum % 3 == 0:
                    ans = max(ans, currSum)
                choose(j + 1)
                currSum -= nums[j]

        choose(0)
        return ans

sol = Solution()
sol.maxSumDivThree([4,1,5,3,1]) # 12
sol.maxSumDivThree([3,6,5,1,8]) # 18
sol.maxSumDivThree([4]) # 0
sol.maxSumDivThree([1,2,3,4,4]) # 12
