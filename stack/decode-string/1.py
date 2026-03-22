"""
Problem: https://leetcode.com/problems/decode-string
Idea:
See number, append to currNum, push current string to string stack
See [, push currNum to int stack > start parsing string
While ], pop int stack and string stack, append currStr to ans

3   currNum = '3'   intStack = []   currStr = ''    stringStack = ['']
[   currNum = ''    intStack = [3]  currStr = ''    stringStack = []
a   currNum = ''    intStack = [3]  currStr = 'a'   stringStack = []
]   currNum = ''    intStack = [3]  currStr = ''   stringStack = ['a']

Time: O(N)
Space: O(N)
"""

class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        currStr = ''
        intStack = []
        stringStack = []

        while i < len(s):
            char = s[i]
            if char.isdigit():
                currNum = 0
                while s[i].isdigit(): 
                    currNum = currNum * 10 + int(s[i])
                    i += 1
                intStack.append(currNum)

            elif char == '[':
                stringStack.append(currStr)
                currStr = ''
                i += 1

            elif char == ']':
                stringStack[-1] += currStr * intStack.pop()
                currStr = stringStack.pop()
                i += 1
            else:
                currStr += char
                i += 1

        return currStr

sol = Solution()

sol.decodeString("sd2[f2[e]g]i")
sol.decodeString("2[3[a2[c]]zz2[def]]")
sol.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef")
sol.decodeString("3[a2[c]]")
sol.decodeString("3[a]2[bc]")
sol.decodeString("2[abc]3[cd]ef")
