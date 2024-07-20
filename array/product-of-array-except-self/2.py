from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        suffix = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            res[i] = res[i] * suffix
            suffix *= nums[i]
        return res
    
solution = Solution()
solution.productExceptSelf([1,2,3,4]) # [24,12,8,6]
solution.productExceptSelf([-1,1,0,-3,3]) # [0,0,9,0,0]