"""
Problem: https://leetcode.com/problems/binary-gap
Idea: AND 1 then shift right
Time: O(logN)
Space: O(1)
"""

class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        curr = 0
        last = -1
        if n & 1:
            last = 0

        while n:
            if n & 1:
                if last >= 0:
                    ans = max(ans, curr - last)
                last = curr
            n >>= 1
            curr += 1
        return ans

sol = Solution()
sol.binaryGap(0)
sol.binaryGap(1)
sol.binaryGap(2)
sol.binaryGap(15)
sol.binaryGap(3204)
sol.binaryGap(22)
sol.binaryGap(8)
sol.binaryGap(5)
