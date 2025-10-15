import math
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        l = 0
        result = math.inf
        for r, num in enumerate(nums):
            total += num
            while total >= target:
                result = min(result, r - l + 1)
                total -= nums[l]
                l += 1

        return 0 if math.isinf(result) else int(result)

sol = Solution()
sol.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]) # 2
sol.minSubArrayLen(target = 4, nums = [1,4,4]) # 1
sol.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]) # 0