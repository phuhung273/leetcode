"""
Problem: https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n
Idea:

3, 9
["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]

4 start with a/b/c
-> Base on k, we can identify 1st char
abab
abac
abca
abcb
acab
acac
acba
acbc
-> 8

--> formula: 2^(n - 1)

Dry-run:
n = 3, k = 9, pool = (a,b,c)
8 < 9 < 12 -> 1st char is c

n = 2, k = 1, pool = (a, b)
1 <= 1 < 2 -> 2nd char is a

n = 1, k = 0, pool = (b, c)
0 <= 0 < 1 -> 3rd char is b

--> cab

Time: O(N)
Space: O(1)
"""

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * 2**(n - 1):
            return ''

        ans = ''
        pool = ['a', 'b', 'c']
        k -= 1

        while n > 1:
            window = 2**(n - 1)
            char = pool[k // window]
            ans += char

            if char == 'a':
                pool = ['b', 'c']
            elif char == 'b':
                pool = ['a', 'c']
            else:
                pool = ['a', 'b']
            k %= window
            n -= 1
        
        ans += pool[k]
            
        return ans

sol = Solution()
sol.getHappyString(6, 70) # cabcac
sol.getHappyString(10, 100) # abacbabacb
sol.getHappyString(1, 1) # a
sol.getHappyString(1, 2) # b
sol.getHappyString(4, 3) # abca
sol.getHappyString(4, 7) # acba
sol.getHappyString(1, 3) # c
sol.getHappyString(1, 4) # ""
sol.getHappyString(3, 9) # "cab"
