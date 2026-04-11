"""
Problem: https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i
Idea: Use a map containing indices of a value
Dry run:
[1,2,1,1,3]

{
    1: [0]
}
{
    1: [0],
    2: [1],
}
{
    1: [0, 2],
    2: [1],
}
{
    1: [0, 2, 3], => compare ans
    2: [1],
}

Time: O(N)
Space: O(distinct values)
"""

from collections import defaultdict
import math
from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        ans = math.inf
        indicesMap = defaultdict(list)

        for i, num in enumerate(nums):
            if len(indicesMap[num]) < 2:
                indicesMap[num].append(i)
            else:
                ans = min(ans, (i - indicesMap[num][0]) * 2)
                indicesMap[num] = [indicesMap[num][1], i]

        return -1 if ans == math.inf else ans # type: ignore

sol = Solution()
sol.minimumDistance([1,2,1,1,3]) # 6
sol.minimumDistance([1,1,2,3,2,1,2]) # 8
sol.minimumDistance([1]) # -1
