"""
Problem: https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix
Idea:
Time to find longest common prefix of 2 integers a and b: O(log(max(a,b))
How: /10 to find all digits, then iterate and check

Brute force: Check prefix of all pairs
Time: mnlog(max(arr1,arr2))
Space: log(max(arr1) + log(arr2))

---------------------------------
For each element of arr1, /10 and add to a set
For each element of arr2, /10 and check existence in set.
Time: mlog(max(arr1)) + nlog(max(arr2))
Space: max(mlog(max(arr1)), nlog(max(arr2)))
"""

import math
from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()

        for num in arr1:
            while num != 0:
                prefixes.add(num)
                num //= 10

        maxPrefix = 0

        for num in arr2:
            while num != 0:
                if num in prefixes:
                    maxPrefix = max(num, maxPrefix)
                num //= 10

        if maxPrefix == 0:
            return 0

        ans = math.log10(maxPrefix)
        return int(ans) + 1

sol = Solution()
# sol.longestCommonPrefix(arr1 = [1,10,100,1000], arr2 = [1000]) # 4
sol.longestCommonPrefix(arr1 = [1,10,999], arr2 = [999]) # 3
sol.longestCommonPrefix(arr1 = [1,10,100], arr2 = [1000]) # 3
sol.longestCommonPrefix(arr1 = [1,2,3], arr2 = [4,4,4]) # 0
