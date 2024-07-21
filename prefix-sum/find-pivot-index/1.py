from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre,suf = [0] * len(nums), [0] * len(nums)
        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] + nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            suf[i] = suf[i + 1] + nums[i + 1]
        for i in range(len(nums)):
            if pre[i] == suf[i]:
                return i
        return -1
    
sol = Solution()
sol.pivotIndex([1,7,3,6,5,6]) # 3
sol.pivotIndex([1,2,3]) # -1
sol.pivotIndex([2,1,-1]) # 0