# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def traverse(node, count):
            if not node:
                return count

            left = traverse(node.left, count + 1)
            right = traverse(node.right, count + 1)
            return max(left, right)
        
        result = traverse(root, 0)
        return result

sol = Solution()
sol.maxDepth(
    TreeNode(3,
        TreeNode(9), TreeNode(20,
                              TreeNode(15), TreeNode(7)
                              )
    )
)

sol.maxDepth(
    TreeNode(3,
        None, TreeNode(2)
    )
)