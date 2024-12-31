from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = n * (n + 1) / 2
        for num in nums:
            result -= num
        return int(result)

solution = Solution()
# solution.missingNumber([3,0,1]) # 2
# solution.missingNumber([0,1]) # 2
solution.missingNumber([0]) # 1
solution.missingNumber([1]) # 0
# solution.missingNumber([9,6,4,2,3,5,7,0,1]) # 8