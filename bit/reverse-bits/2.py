"""
Problem: https://leetcode.com/problems/reverse-bits
Idea:
bit at index i: (n >> i) & 1
Write bit to ans: ans |= (bit at index i)
ans >> 1
Time: O(1)
Space: O(1)
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans |= (n >> i) & 1
            if i == 31:
                break
            ans <<= 1
        return ans

sol = Solution()
sol.reverseBits(43261596) # 964176192
sol.reverseBits(2147483644) # 1073741822
