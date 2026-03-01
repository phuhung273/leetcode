"""
Problem: https://leetcode.com/problems/total-cost-to-hire-k-workers
Idea: Keep leftHeap and rightHeap, left and right pointers
Time: O(KlogC + ClogC)
Space: O(C)
"""

import heapq
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if k > len(costs):
            return sum(costs)
        
        leftHeap, rightHeap = [], []
        left = candidates - 1
        right = max(left + 1, len(costs) - candidates)

        for i in range(candidates):
            heapq.heappush(leftHeap, costs[i])
        for i in range(len(costs) - 1, right - 1, - 1):
            heapq.heappush(rightHeap, costs[i])
        
        ans = 0

        for _ in range(k):
            if not rightHeap or (leftHeap and leftHeap[0] <= rightHeap[0]):
                ans += heapq.heappop(leftHeap)
                left += 1
                if left < right:
                    heapq.heappush(leftHeap, costs[left])
            else:
                ans += heapq.heappop(rightHeap)
                right -= 1
                if right > left:
                    heapq.heappush(rightHeap, costs[right])

        return ans

sol = Solution()
sol.totalCost([57,33,26,76,14,67,24,90,72,37,30], 11, 2) # 526
sol.totalCost([69,10,63,24,1,71,55,46,4,61,78,21,85,52,83,77,42,21,73,2,80,99,98,89,55,94,63,50,43,62,14], 21, 31) # 829
sol.totalCost([28,35,21,13,21,72,35,52,74,92,25,65,77,1,73,32,43,68,8,100,84,80,14,88,42,53,98,69,64,40,60,23,99,83,5,21,76,34], 32, 12) # 1407
sol.totalCost([31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58], 11, 2) # 423
# sol.totalCost([], 2, 2) # 3
sol.totalCost([3,2,7,7,1,2], 2, 2) # 3
sol.totalCost(costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4) # 11
sol.totalCost(costs = [1,2,4,1], k = 3, candidates = 3) # 4
