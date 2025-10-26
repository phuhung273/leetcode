"""
Get bit at x of n: (num >> x) & 1
Get 1st bit of n: n & 1
Set i bit of n to 1: n |= (1 << i)
Set i bit of n to 0: n & (~(1 << i))
"""

class Solution:
    def findComplement(self, num: int) -> int:
        result = 1
        i = 0
        while num != 0:
            flipped = (num & 1) ^ 1
            if flipped == 1:
                result |= 1 << i
            else:
                result &= ~(1 << i)

            num >>= 1
            i += 1
        return result

sol = Solution()
sol.findComplement(2)
sol.findComplement(5)
sol.findComplement(1)
