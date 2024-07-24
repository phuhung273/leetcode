from typing import List
from queue import PriorityQueue

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = PriorityQueue()
        for num in nums:
            pq.put((-num, num))
        for i in range(k):
            result = pq.get()[1]
        return result
    
sol = Solution()
# sol.findKthLargest([3,2,1,5,6,4], 2) # 5
# sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4) # 4
sol.findKthLargest([-2,-1,1,-4], 2) # -1