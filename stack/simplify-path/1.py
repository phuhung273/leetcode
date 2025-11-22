"""
Problem: https://leetcode.com/problems/simplify-path

Idea:
Keep a var curr
/ is delimiter
When see delimiter, append curr to stack
If curr == '.', skip
If curr == '..', pop

Time: O(N)
Space: O(N)
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr = ''
        path += '/'

        for char in path:
            if char != '/':
                curr += char
                continue
            if curr == '':
                continue
            if curr == '..' and len(stack) > 0:
                stack.pop()
            if curr != '.' and curr != '..':
                stack.append(curr)
            curr = ''

        return '/' + '/'.join(stack)

sol = Solution()
sol.simplifyPath("/") # /
sol.simplifyPath("/..") # /
sol.simplifyPath("/...") # /...
# sol.simplifyPath("/home/") # /home
# sol.simplifyPath("/home//foo/") # /home/foo
# sol.simplifyPath("/home/user/Documents/../Pictures") # /home/user/Pictures
sol.simplifyPath("/../") # /
sol.simplifyPath("/.../a/../b/c/../d/./") # /.../b/d
