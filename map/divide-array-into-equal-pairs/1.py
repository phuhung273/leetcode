from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        memo = {}
        for num in nums:
            memo[num] = memo.get(num, 0) + 1

        for key in memo:
            if memo[key] % 2 != 0:
                return False

        return True

sol = Solution()
sol.divideArray([3,2,3,2,2,2]) # True
sol.divideArray([1,2,3,4]) # False