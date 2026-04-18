"""
Problem: https://leetcode.com/problems/mirror-distance-of-an-integer
Idea:
Brute force: modulo then //= 10
Time: O(logN)
Space: O(1)
"""

class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev = 0
        temp = n
        while temp != 0:
            rev *= 10
            newTemp = temp // 10
            rev += temp - newTemp * 10
            temp = newTemp
        
        return abs(n - rev)

sol = Solution()
sol.mirrorDistance(25) # 27
sol.mirrorDistance(10) # 9
sol.mirrorDistance(7) # 9
