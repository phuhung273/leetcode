from typing import List
import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        queue = []
        for i in range(len(nums)):
            heapq.heappush(queue, (nums[i], i))
        
        for _ in range(k):
            min_val, min_index = heapq.heappop(queue)
            nums[min_index] = min_val * multiplier
            heapq.heappush(queue, (nums[min_index], min_index))

        return nums

solution = Solution()
solution.getFinalState([2,1,3,5,6], 5, 2) # [8,4,6,5,6]
solution.getFinalState([1,2], 3, 4) # [16,8]