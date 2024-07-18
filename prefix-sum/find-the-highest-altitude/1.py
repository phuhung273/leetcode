from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result,current = 0,0
        for diff in gain:
            current += diff
            result = max(result, current)
        return result
    
solution = Solution()
solution.largestAltitude([-5,1,5,0,-7]) # 1
solution.largestAltitude([-4,-3,-2,-1,4,3,2]) # 0