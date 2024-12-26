from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonZeroIndex = 0
        for num in nums:
            if num != 0:
                nums[nonZeroIndex] = num
                nonZeroIndex += 1
        
        for i in range(nonZeroIndex, len(nums)):
            nums[i] = 0
        
solution = Solution()
solution.moveZeroes([0,1,0,3,12]) # [1,3,12,0,0]