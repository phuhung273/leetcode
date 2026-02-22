"""
Problem: https://leetcode.com/problems/container-with-most-water
Idea: Use left and right pointers
Move lower pointer inward

Why this works: can an inner left combine with outter right forms a better result

Outter right was passed because it is less than something on the left
        l   r   passed because 8 < 10
[10     3   5   8]

    l                               r
    1   8   6   2   5   4   8   3   7
ans = 8

        l                           r
    1   8   6   2   5   4   8   3   7
ans = 49

Time: O(N)
Space: O(1)
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            ans = max(ans, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans

sol = Solution()
sol.maxArea([1,8,6,2,5,4,8,3,7]) # 49
sol.maxArea([10,3,5,8]) # 24
sol.maxArea([1,10,5,8]) # 16
sol.maxArea([1,1]) # 1
