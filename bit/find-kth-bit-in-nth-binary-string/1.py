"""
Problem: https://leetcode.com/problems/find-kth-bit-in-nth-binary-string
Idea: invert ~
011 > invert > 100 > reverse 001

0111001 > invert > 1000110 > reverse > 0110001

Integer of all bits set to 1 with bit length n: 2^n - 1

Optimization: after n operations, k will be at bitLen - k
So we only need to generate until that step

Time:
Space:
"""

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        bitLen = 1
        last = 0

        def reverseBits(n, length: int):
            left, right = length - 1, 0
            while left > right:
                leftBit = (n >> left) & 1
                rightBit = (n >> right) & 1

                if leftBit != rightBit:
                    n ^= (1 << left)
                    n ^= (1 << right)
                left -= 1
                right += 1
            return n

        for _ in range(n):
            mask = 2**bitLen - 1
            inv = last ^ mask
            last <<= 1
            last += 1
            last <<= bitLen
            last += reverseBits(inv, bitLen)
            bitLen = 2*bitLen + 1

        return str((last >> (bitLen - k)) & 1)

sol = Solution()
sol.findKthBit(20, 1048575) # 1
sol.findKthBit(3, 1) # 0
sol.findKthBit(4, 11) # 1
