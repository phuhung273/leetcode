from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        prefixSum = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            if i == k - 1:
                result = prefixSum / k
            elif i > k - 1:
                prefixSum -= nums[i - k]
                if nums[i] > nums[i - k]:
                    result = max(prefixSum / k, result)

        return result
    
solution = Solution()
# solution.findMaxAverage([5], 1) # 5
solution.findMaxAverage([1,12,-5,-6,50,3], 4) # 12.75
solution.findMaxAverage([1,2,3,4,5,6], 3) # 5