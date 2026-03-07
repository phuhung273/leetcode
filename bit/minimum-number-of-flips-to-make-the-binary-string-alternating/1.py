"""
Problem: https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating
Idea: Try to use type 1 as much as possible
If s[left] == s[left + 1] and s[left] != s[right]: type 1, right = left, left += 1

1   1   1   0   0   0
> Type 1
1   1   0   0   0   1
> Type 2
0   1   0   0   0   1
> Type 1
1   0   0   0   1   0
> Type 1
0   0   0   1   0   1
> Type 1
0   0   1   0   1   0
> Type 2
1   0   1   0   1   0


s[left] == s[left + 1] and s[left] == s[right] ---> type 2, right = left, left += 1
1   1   ... 1

s[left] != s[left + 1] and s[left] != s[right] ---> type 1, right = left, left += 1
1   0   ... 0

s[left] != s[left + 1] and s[left] == s[right] ---> 
1   0   ... 1

------------------------------

zeroEven
zeroOdd
oneEven
oneOdd

Type 1: swap zeroOdd <-> zeroEven, oneOdd <-> oneEven

Difference between zeroOdd and oneEven (3), zeroEven and oneOdd (4)

Double the string, slide a window of size n.

0   1   0   0   1   0   0   1   1   0   1           zeroEven=3, zeroOdd=3
    1   0   0   1   0   0   1   1   0   1   0       zeroEven=4, zeroOdd=2

Time: O(N)
Space: O(1)
"""

class Solution:
    def minFlips(self, s: str) -> int:
        zeroOdd, zeroEven, oneOdd, oneEven = 0, 0, 0, 0

        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == '0':
                    zeroEven += 1
                else:
                    oneEven += 1
            else:
                if s[i] == '0':
                    zeroOdd += 1
                else:
                    oneOdd += 1

        ans = min(
            # Start with 0
            zeroOdd + oneEven,
            # Start with 1
            zeroEven + oneOdd,
        )

        for i in range(len(s)):
            zeroOdd, zeroEven, oneOdd, oneEven = zeroEven, zeroOdd, oneEven, oneOdd

            if len(s) % 2 == 1:
                if s[i] == '0':
                    zeroOdd -= 1
                    zeroEven += 1
                else:
                    oneOdd -= 1
                    oneEven += 1

            ans = min(
                ans,
                # Start with 0
                zeroOdd + oneEven,
                # Start with 1
                zeroEven + oneOdd,
            )

        return ans

sol = Solution()
sol.minFlips("01001001101") # 2
sol.minFlips("111000") # 2
sol.minFlips("010") # 0
sol.minFlips("1110") # 1
