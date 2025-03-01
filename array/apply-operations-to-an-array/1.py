from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        count = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                result[count] = nums[i] * 2
                nums[i + 1] = 0
            else:
                result[count] = nums[i]
            count += 1

        return result

sol = Solution()
sol.applyOperations([1,2,2,1,1,0]) # [1,4,2,0,0,0]
sol.applyOperations([0,1]) # [1,0]