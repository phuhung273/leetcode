"""
Problem: https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers
Idea: Iterate from 1 to n, count bit of current > shift left > OR operation
Optimize: save count and update after every iteration
Time: O(N) as n <= 10^5 then bitCount <= 17
Space: O(1)
"""

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 0
        mod = 10**9 + 7
        bitCount = 1
        nextBit = 2
        for i in range(1, n + 1):
            if i >= nextBit:
                bitCount += 1
                nextBit = pow(2, bitCount, mod)
            ans <<= bitCount
            ans |= i
            ans %= mod
        return ans

sol = Solution()
sol.concatenatedBinary(1) # 1
sol.concatenatedBinary(3) # 27
sol.concatenatedBinary(12) # 505379714
