"""
Problem: https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree
Idea: DFS with boolean isRight
Time: O(N)
Space: O(H)
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode], isRight: bool, curr: int):
            nonlocal ans
            if not node:
                return

            ans = max(ans, curr)
            if isRight:
                dfs(node.left, False, curr + 1)
                dfs(node.right, True, 1)
            else:
                dfs(node.left, False, 1)
                dfs(node.right, True, curr + 1)

        if root:
            dfs(root.right, True, 1)
            dfs(root.left, False, 1)
        return ans

sol = Solution()
sol.longestZigZag(TreeNode(1, right=TreeNode(1, TreeNode(1), TreeNode(1, TreeNode(1, right=TreeNode(1, right=TreeNode(1))), TreeNode(1))))) # 3
sol.longestZigZag(TreeNode(1, TreeNode(1, right=TreeNode(1, TreeNode(1, right=TreeNode(1)), TreeNode(1))), TreeNode(1))) # 4
