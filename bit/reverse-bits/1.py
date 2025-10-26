"""
Idea: 2 pointers
If left != right, flip bit of left and right

Flit bit at x: n = n ^ (1 << x)
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        left, right = 31, 0
        while left > right:
            i = (n >> left) & 1
            j = (n >> right) & 1

            if i != j:
                n = n ^ (1 << left)
                n = n ^ (1 << right)

            left -=1
            right +=1
        return n

sol = Solution()
sol.reverseBits(43261596)
sol.reverseBits(2147483644)
