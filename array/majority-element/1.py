from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if count == 0:
                current = num

            if num != current:
                count -= 1
            elif num == current:
                count += 1
            
        return current

solution = Solution()
solution.majorityElement([3,2,3]) # 3
solution.majorityElement([2,2,1,1,1,2,2]) # 2