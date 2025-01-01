class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        result = 0
        isPrimeMap = {}
        for num in range(2, n):
            if num not in isPrimeMap:
                result += 1
                isPrimeMap[num] = True

                multiplier = num
                while True:
                    if num * multiplier > n:
                        break

                    isPrimeMap[num * multiplier] = False
                    multiplier += 1

        return result


solution = Solution()
# solution.countPrimes(10) # 4
solution.countPrimes(500000) # 4