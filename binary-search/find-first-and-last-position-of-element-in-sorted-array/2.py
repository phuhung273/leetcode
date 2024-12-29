from typing import List
import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1, -1]
        left = bisect.bisect_left(nums, target)

        if left >= len(nums) or nums[left] != target:
            return [-1, -1]

        right = bisect.bisect_right(nums, target,lo=left) - 1
        return [left, right]

solution = Solution()
solution.searchRange([5,7,7,8,8,10], 8) # [3,4]
solution.searchRange([5,7,7,8,8,10], 6) # [-1,-1]
solution.searchRange([], 0) # [-1,-1]
solution.searchRange([2,2], 3) # [-1,-1]