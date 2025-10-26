"""
Idea:
n:          xxxxxxxxxx1000000
n - 1:      xxxxxxxxxx0111111
n & n - 1:  xxxxxxxxxx0000000

=> n & n - 1 will flip right most 1 to 0
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n != 0:
            result += 1
            n = n & n - 1
        return result

sol = Solution()
sol.hammingWeight(11)
sol.hammingWeight(128)
sol.hammingWeight(2147483645)
