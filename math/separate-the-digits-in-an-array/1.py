"""
Problem: https://leetcode.com/problems/separate-the-digits-in-an-array
Idea: Modulo 10 then // 10
Time: O(NlogM) where M is max of nums
Space: O(logM)

---
Idea: convert int to string > append
Time: O(NlogM) where M is max of nums
Space: O(1)
---
Idea: Same as 1st solution but traverse nums reversely
Time: O(NlogM) where M is max of nums
Space: O(1)
"""

from typing import List


class Solution:
    # def separateDigits(self, nums: List[int]) -> List[int]:
    #     ans = []

    #     for num in nums:
    #         for char in str(num):
    #             ans.append(int(char))
    #     return ans
    
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            while num != 0:
                ans.append(num % 10)
                num //= 10
        ans.reverse()
        return ans

sol = Solution()
sol.separateDigits([13,25,83,77])
sol.separateDigits([7,1,3,9])
