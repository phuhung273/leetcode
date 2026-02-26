"""
Problem: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one
Idea:
Divide 2: +1 and move left
Add 1: +2 steps > incorrect as it will modify next bit

Fix: when odd, isIncrease = True
When isIncrease:
- even become odd > isIncrease=False
- odd become even

Convert to integer > inefficient as s has 500 bits
Time: O(N)
Space: O(1)
"""

class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        arr = list(s)
        arr.reverse()

        i = 0
        while i < len(arr) - 1:
            if arr[i] == '0':
                ans += 1
            else:
                ans += 2
                if arr[i + 1] == '0':
                    arr[i + 1] = '1'
                else:
                    j = i + 1
                    while j < len(arr) and arr[j] == '1':
                        arr[j] = '0'
                        j += 1

                    if j < len(arr):
                        arr[j] = '1'
                    else:
                        arr.append('1')
            i += 1

        return ans

sol = Solution()
sol.numSteps("11111") # 6
"""
10000, ans = 2
1, ans = 6
"""
sol.numSteps("11011") # 7
"""
1100, ans = 2
11, ans = 4
100, ans = 5
1, ans = 7
"""
sol.numSteps("11001") # 8
"""
1101, ans = 2
"""
sol.numSteps("1101") # 6
sol.numSteps("10") # 1
sol.numSteps("1") # 0
