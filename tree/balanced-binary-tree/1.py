# type: ignore
"""
Problem: https://leetcode.com/problems/balanced-binary-tree
Idea: DFS and compare left right

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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            
            left = dfs(node.left)
            if left == -1:
                return -1
            right = dfs(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return - 1
            return max(left, right) + 1
        
        ans = dfs(root)
        return ans != -1

sol = Solution()
sol.isBalanced(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
sol.isBalanced(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2)))
