# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.result = 0

        def traverse(node, maximum):
            if not node: return

            if node.val >= maximum:
                self.result += 1
                maximum = node.val

            traverse(node.left, maximum)
            traverse(node.right, maximum)

        traverse(root, -math.inf)
        return self.result

sol = Solution()

sol.goodNodes(
    TreeNode(9, None,
        TreeNode(3, TreeNode(6)),
    )
) # 1

sol.goodNodes(
    TreeNode(3,
        TreeNode(1, TreeNode(3)),
        TreeNode(4, TreeNode(1), TreeNode(5))
    )
) # 4

sol.goodNodes(
    TreeNode(3,
        TreeNode(3, TreeNode(4), TreeNode(2)),
    )
) # 3

sol.goodNodes(TreeNode(1)) # 1