"""
Problem: https://leetcode.com/problems/binary-number-with-alternating-bits
Idea: Save a var lastBit after every iteration
Time: O(logN)
Space: O(1)
"""

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        lastBit = n & 1
        n >>= 1
        while n != 0:
            bit = n & 1
            if bit == lastBit:
                return False
            lastBit = bit
            n >>= 1
        return True

sol = Solution()
sol.hasAlternatingBits(5) # true
sol.hasAlternatingBits(7) # false
sol.hasAlternatingBits(11) # false
sol.hasAlternatingBits(42) # true
