"""
Problem: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers
Idea: DFS with global curr, shift left every level
Time: O(N)
Space: O(height)
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0
        curr = 0

        def dfs(node: Optional[TreeNode]):
            nonlocal ans, curr

            if not node:
                return
            
            curr = (curr << 1) | node.val

            if node.left or node.right:
                dfs(node.left)
                dfs(node.right)
            else:
                ans += curr
            curr >>= 1

        dfs(root)
        return ans

sol = Solution()
sol.sumRootToLeaf(TreeNode(1, TreeNode(0, TreeNode(0), TreeNode(1)), TreeNode(1, TreeNode(0), TreeNode(1))))
