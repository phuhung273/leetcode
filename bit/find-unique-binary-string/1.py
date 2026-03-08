"""
Problem: https://leetcode.com/problems/find-unique-binary-string
Idea:
XOR > doesn't work because it only find the odd number of ith bit

Findings:
- Total: 2^n
- Add all of them to a set
- From 0 to 2^n, return 1st num not in the set

Time: O(2^n)
Space: O(len(nums))

------------------------------

With full: even number of 0, even number of 1
If something is missing, then some position will have an odd number of 0 or 1
If we XOR everything, and ith position is 1 > miss a 1
Else if it is 0, miss a 0
"""

from typing import List


class Solution:
    # def findDifferentBinaryString(self, nums: List[str]) -> str:
    #     n = len(nums[0])
    #     existSet = set()

    #     for num in nums:
    #         existSet.add(int(num, 2))

    #     for i in range(2 << n):
    #         if i not in existSet:
    #             ans = bin(i)[2:]

    #             if len(ans) < n:
    #                 ans = '0' * (n - len(ans)) + ans
    #             return ans
    #     return ''

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = ''
        for i in range(len(nums)):
            ans += '0' if nums[i][i] == '1' else '1'
        return ans

sol = Solution()
sol.findDifferentBinaryString(["00","01"])
sol.findDifferentBinaryString(["00","10"])
sol.findDifferentBinaryString(["0"])
sol.findDifferentBinaryString(["01"])
sol.findDifferentBinaryString(["111","011","001", "101"])
sol.findDifferentBinaryString(["01","10"])
sol.findDifferentBinaryString(["111","011","001"])
