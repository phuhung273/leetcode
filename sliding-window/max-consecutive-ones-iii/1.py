from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = result = 0
        queue = []
        firstOIndex = 0

        for i in range(len(nums)):
            num = nums[i]

            if num == 0:
                queue.append(i)

                if len(queue) - firstOIndex > k:
                    left = queue[firstOIndex] + 1
                    firstOIndex += 1

            result = max(result, i - left + 1)
        return result

sol = Solution()
sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) # 10
sol.longestOnes([0,0,0,0,0,0], 2) # 2
sol.longestOnes([1,1,1,1,1,1], 3) # 6
sol.longestOnes([1,1,0,0,0,0], 2) # 4
sol.longestOnes([0,1,1,0,0,0], 2) # 4
sol.longestOnes([0,1,0,1,0,0], 2) # 4
sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2) # 6