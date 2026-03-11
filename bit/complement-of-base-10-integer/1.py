"""
Problem: https://leetcode.com/problems/complement-of-base-10-integer
Idea: Shift and check
Time: O(bitLength)
Space: O(1)

---

Idea: Find allOne containing all 1 and has same bit length with n. ans = allOne - n
Time: O(bitLength)
Space: O(1)
"""

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        return (1 << n.bit_length()) - 1 - n

sol = Solution()
sol.bitwiseComplement(5) # 2
sol.bitwiseComplement(7) # 0
sol.bitwiseComplement(10) # 5
