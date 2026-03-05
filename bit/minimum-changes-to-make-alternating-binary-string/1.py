"""
Problem: https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string
Idea: Min of first is 0 or first is 1
Time: O(N)
Space: O(1)
"""

class Solution:
    def minOperations(self, s: str) -> int:
        firstIs0 = 0
        firstIs1 = 0
        for i in range(len(s)):
            if i % 2 == 0:
                # even
                if s[i] == '1':
                    firstIs0 += 1
                else:
                    firstIs1 += 1
            else:
                # odd
                if s[i] == '1':
                    firstIs1 += 1
                else:
                    firstIs0 += 1
        return min(firstIs0, firstIs1)

sol = Solution()
sol.minOperations("0100") # 1
sol.minOperations("10") # 0
sol.minOperations("1111") # 2
