from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        n = len(nums)

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            suffix[n - 1 - i] = suffix[n - i] * nums[n - i]
        return [prefix[i] * suffix[i] for i in range(n)]

sol = Solution()
# sol.productExceptSelf([1,2,3,4]) # [24,12,8,6]
sol.productExceptSelf([2,3,4,5]) # [60,40,30,24]
# sol.productExceptSelf([-1,1,0,-3,3]) # [0,0,9,0,0]