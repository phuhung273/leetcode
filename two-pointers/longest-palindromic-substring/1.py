"""
Problem: https://leetcode.com/problems/longest-palindromic-substring

Idea:
Move right until s[i] == s[i+1] or s[i-1] = s[i+1]. This is the palindrome center.
From the center, expand left and right until left and right different, compare longest

Time: O(N^2)

Space: O(1)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''

        def check(left, right):
            while left > -1 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        for i in range(len(s)):
            odd_str = check(i, i)
            even_str = check(i, i + 1)
            if len(odd_str) > len(ans):
                ans = odd_str
            if len(even_str) > len(ans):
                ans = even_str

        return ans

sol = Solution()
sol.longestPalindrome("babad")
sol.longestPalindrome("cbbd")
