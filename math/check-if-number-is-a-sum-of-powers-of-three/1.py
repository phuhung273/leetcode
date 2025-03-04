class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n != 1:
            if n % 3 == 0:
                n = n / 3
                continue

            if (n - 1) % 3 != 0:
                return False
            n -= 1
        return True

sol = Solution()
sol.checkPowersOfThree(12) # True
sol.checkPowersOfThree(91) # True
sol.checkPowersOfThree(21) # False
sol.checkPowersOfThree(1) # True