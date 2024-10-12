from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        result = 0
        while left < right:
            current = (right - left) * min(height[right], height[left])
            result = max(current, result)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return result
    
sol = Solution()
sol.maxArea([1,8,6,2,5,4,8,3,7]) # 49
sol.maxArea([1, 1]) # 1
sol.maxArea([8,7,2,1]) # 7