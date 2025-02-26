from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        store = {}
        result = 0

        for num in nums:
            if k - num in store and store[k - num] != 0:
                store[k - num] -= 1
                result += 1
                continue
            
            if num not in store:
                store[num] = 0
            
            store[num] += 1
        return result

sol = Solution()
sol.maxOperations([1,2,3,4], 5) # 2
sol.maxOperations([3,1,3,4,3], 6) # 1