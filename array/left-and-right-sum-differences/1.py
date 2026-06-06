"""
Problem: https://leetcode.com/problems/left-and-right-sum-differences
Idea: Initialize ans array filled with 0
Iterate from 1 to n, fill ans[i] = ans[i - 1] + nums[i - 1]

10  4   8   3
0   10  14  22

Have an int rightSum = 0
Iterate backward, ans[i] -= rightSum
rightSum += nums[i]

10  4   8   3
0   10  14  22

            22
        11
    1
15

Time: O(N)
Space: O(1)
"""

from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        for i in range(1, n):
            ans[i] = ans[i - 1] + nums[i - 1]
        
        rightSum = 0
        for i in range(n - 1, -1, -1):
            ans[i] = abs(ans[i] - rightSum)
            rightSum += nums[i]
        return ans

sol = Solution()
sol.leftRightDifference([10,4,8,3]) # [15,1,11,22]
sol.leftRightDifference([1]) # [0]
