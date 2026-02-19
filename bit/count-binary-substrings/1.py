"""
Problem: https://leetcode.com/problems/count-binary-substrings
Idea: Expand from center
Time: O(N^2)
Space: O(1)
"""

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        for i in range(1, len(s)):
            leftIndex, rightIndex = i - 1, i
            leftValue, rightValue = s[i - 1], s[i]

            while leftIndex >= 0 and rightIndex < len(s) and s[leftIndex] != s[rightIndex] and s[leftIndex] == leftValue and s[rightIndex] == rightValue:
                ans += 1
                leftIndex -= 1
                rightIndex += 1

        return ans

sol = Solution()
sol.countBinarySubstrings("00110011") # 6
sol.countBinarySubstrings("10101") # 4
