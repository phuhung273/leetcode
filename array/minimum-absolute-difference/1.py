"""
Problem: https://leetcode.com/problems/minimum-absolute-difference

Idea: sort and find minimum difference

Time: O(sortN)
Space: O(sortN)
"""

import math
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff = math.inf
        ans = []

        for i in range(len(arr) - 1):
            if arr[i + 1] == arr[i]:
                continue
            elif arr[i + 1] - arr[i] < diff:
                diff = arr[i + 1] - arr[i]
                ans = [[arr[i], arr[i + 1]]]
            elif arr[i + 1] - arr[i] == diff:
                ans.append([arr[i], arr[i + 1]])
        return ans

sol = Solution()
sol.minimumAbsDifference([4,2,1,3])
sol.minimumAbsDifference([1,3,6,10,15])
sol.minimumAbsDifference([3,8,-10,23,19,-4,-14,27])
