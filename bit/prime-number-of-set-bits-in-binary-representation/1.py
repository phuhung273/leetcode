"""
Problem: https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation
Idea:
10^6 has maximum 19 bits set
For each numbers in [left, right], check if its bit sets is [2,3,5,7,11,13,17,19]

Time: O(Nlog(N))
Space: O(1)
"""

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = set([2,3,5,7,11,13,17,19])

        def checkBitsSet(n: int) -> bool:
            count = 0
            while n != 0:
                count += 1
                n &= (n - 1)
            if count in primes:
                return True
            return False

        ans = 0
        for i in range(left, right + 1):
            if checkBitsSet(i):
                ans += 1
        return ans

sol = Solution()
sol.countPrimeSetBits(6, 10) # 4
sol.countPrimeSetBits(10, 15) # 5
