from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j = 0,0
        while i < len(nums) and nums[i] != 0:
            i += 1

        j = i + 1
        while j < len(nums):
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1

            
        
solution = Solution()
# solution.moveZeroes([0,1,0,3,12]) # [1,3,12,0,0]
# solution.moveZeroes([0]) # [0]
# solution.moveZeroes([1]) # [1]
# solution.moveZeroes([1,0]) # [1,0]
solution.moveZeroes([1,0,1]) # [1,1,0]