"""
Problem: https://leetcode.com/problems/add-binary
Idea:
Time: O(N)
Space: O(N)
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == '0':
            return b
        elif b == '0':
            return a

        short = a if len(b) >= len(a) else b
        long = a if len(a) > len(b) else b
        lenDiff = len(long) - len(short)
        ans = []
        isIncrease = False

        for i in range(len(short) - 1, -1, -1):
            if long[i + lenDiff] == '1' and short[i] == '1':
                if isIncrease:
                    ans.append('1')
                else:
                    ans.append('0')
                    isIncrease = True
            elif long[i + lenDiff] == '0' and short[i] == '0':
                if isIncrease:
                    ans.append('1')
                    isIncrease = False
                else:
                    ans.append('0')
            else:
                if isIncrease:
                    ans.append('0')
                    isIncrease = False
                else:
                    ans.append('1')

        for i in range(lenDiff - 1, -1, -1):
            if not isIncrease:  
                ans.append(long[i])
            else:
                if long[i] == '0':
                    ans.append('1')
                    isIncrease = False
                else:
                    ans.append('0')

        if isIncrease:
            ans.append('1')
        ans.reverse()
        return ''.join(ans)

sol = Solution()
sol.addBinary('100', '110010') # 100
# sol.addBinary('11', '1') # 100
# sol.addBinary('11', '11') # 110
sol.addBinary('1010', '1011') # 10101
