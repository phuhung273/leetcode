"""
Problem: https://leetcode.com/problems/basic-calculator-ii
Idea: Stack
Optimization:
- No point saving 2 consecutive ++,+-,-+ > Space is now O(1)
- Stack never has more than 4 elements
Time: O(N)
Space: O(1)
"""

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0

        while i < len(s):
            char = s[i]

            if char == ' ':
                i += 1
                continue
            elif char.isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = 10 * num + int(s[i])
                    i += 1

                if stack and stack[-1] == '*':
                    stack.pop()
                    stack.append(num * stack.pop())
                elif stack and stack[-1] == '/':
                    stack.pop()
                    stack.append(int(stack.pop() / num))
                else:
                    stack.append(num)
            else:
                if char in ['+', '-'] and len(stack) >= 3 and stack[-2] in ['+', '-']:
                    a = stack.pop()
                    sign = stack.pop()
                    b = stack.pop()

                    if sign == '+':
                        stack.append(a + b)
                    else:
                        stack.append(b - a)
                stack.append(char)
                i += 1
        
        num = 0
        sign = True
        for element in stack:
            if element == '+':
                sign = True
            elif element == '-':
                sign = False
            else:
                if sign:
                    num += element
                else:
                    num -= element
        return num

sol = Solution()
sol.calculate("3+2+2") # 7
sol.calculate("3+22*2") # 47
sol.calculate("3+2*2") # 7
sol.calculate(" 3/2 ") # 1
sol.calculate(" 3+5 / 2 ") # 5
