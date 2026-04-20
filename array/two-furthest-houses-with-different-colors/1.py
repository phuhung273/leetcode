"""
Problem: https://leetcode.com/problems/two-furthest-houses-with-different-colors
Idea:
Brute force: for every house, find from the outside the furthest different color
Time: O(N^2)
Space: O(1)
-------------------------
Left and right pointer.
If left != right, return right - left
Else:
    if left != left + 1:
        left += 1
    else:
        right -= 1
This will prioritize shifting left. But the answer might be prioritizing shifting right
So we run another round
Time: O(N)
Space: O(1)
"""

from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        left, right = 0, len(colors) - 1

        while colors[left] == colors[right]:
            if colors[left] != colors[left + 1]:
                left += 1
            else:
                right -= 1

        ans = right - left
        left, right = 0, len(colors) - 1
        while colors[left] == colors[right]:
            if colors[right] != colors[right - 1]:
                right -= 1
            else:
                left += 1
        ans = max(ans, right - left)
        return ans

sol = Solution()
sol.maxDistance([1,1,6,1,1,1,1]) # 4
sol.maxDistance([1,6,1,1,1,1,1]) # 5
sol.maxDistance([1,1,1,6,1,1,1]) # 3
sol.maxDistance([1,8,3,8,3]) # 4
sol.maxDistance([0,1]) # 1
