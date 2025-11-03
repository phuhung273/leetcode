# type: ignore
"""
Problem: https://leetcode.com/problems/maximum-score-of-a-good-subarray

Idea:

Use 2 new left and right array to save closest left/right index that is less than nums[i]

Subproblem: Find array containing closest left index that is less than nums[i]
[2 5 3 6]
[0 1 1 3]

        [2 2 2 3 4]
left  = [0 0 0 3 4]
right = [4 4 4 4 4]

Time: O(N)

Space: O(N)
"""

from collections import deque
import math
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left = [-1] * len(nums)
        stack = deque()

        for i in range(len(nums)):
            while len(stack) > 0 and nums[i] <= nums[stack[0]]:
                stack.popleft()
            if len(stack) == 0:
                left[i] = 0
            else:
                left[i] = stack[0] + 1
            stack.appendleft(i)

        right = [-1] * len(nums)
        stack = deque()

        for i in range(len(nums) - 1, -1, -1):
            while len(stack) > 0 and nums[i] <= nums[stack[0]]:
                stack.popleft()
            if len(stack) == 0:
                right[i] = len(nums) - 1
            else:
                right[i] = stack[0] - 1
            stack.appendleft(i)
        
        result = -math.inf
        for i in range(len(nums)):
            if k >= left[i] and k <= right[i]:
                result = max(result, (right[i] - left[i] + 1) * nums[i])

        return result

sol = Solution()
# #                          0    1    2    3    4    5   6    7    8    9
# sol.maximumScore(nums = [6569,9667,3148,7698,1622,2194,793,9041,1670,1872], k = 5) # 9732
# sol.maximumScore(nums = [1,4,3,7,4,5], k = 3) # 15
sol.maximumScore(nums=[2,2,2,3,4], k=1) # 10
sol.maximumScore(nums = [5,5,4,5,4,1,1,1], k = 0) # 20
