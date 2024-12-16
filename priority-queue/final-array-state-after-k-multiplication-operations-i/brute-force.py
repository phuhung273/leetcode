from typing import List

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            smallest_idx = self.find_smallest_idx(nums)
            nums[smallest_idx] = nums[smallest_idx] * multiplier
        return nums
    
    def find_smallest_idx(self, nums: List[int]) -> int:
        idx = 0
        smallest = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < smallest:
                smallest = nums[i]
                idx = i
        return idx

solution = Solution()
solution.getFinalState([2,1,3,5,6], 5, 2) # [8,4,6,5,6]
solution.getFinalState([1,2], 3, 4) # [16,8]