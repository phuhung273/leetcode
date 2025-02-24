import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        
        gcdLen = math.gcd(len(str1), len(str2))
        return str1[0 : gcdLen]

solution = Solution()
solution.gcdOfStrings('ABCABC', 'ABC') # ABC
solution.gcdOfStrings('ABABAB', 'ABAB') # AB
solution.gcdOfStrings('LEET', 'CODE') # ''