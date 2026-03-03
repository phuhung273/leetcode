"""
Problem: https://leetcode.com/problems/find-kth-bit-in-nth-binary-string
Idea:

DP: Find bitLen after n operations

If k is mid: return 1
If k is on the left half: dp(n, k) = dp(n - 1, k)
If k is on the right half: dp(n, k) = ~dp(n - 1, k - mid)

Time: O(N)
Space: O(N)
"""

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'

        length = 1 << n
        mid = length // 2
        if k == mid:
            return '1'
        elif k < mid:
            return self.findKthBit(n - 1, k)
        return "0" if self.findKthBit(n - 1, length - k) == "1" else "1"


sol = Solution()
sol.findKthBit(3, 5) # 0
sol.findKthBit(20, 1048575) # 1
sol.findKthBit(3, 1) # 0
sol.findKthBit(4, 11) # 1
