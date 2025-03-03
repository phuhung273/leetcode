# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        result = []

        queue = deque([(0, root)])
        currentDepth = None

        while queue:
            depth, node = queue.popleft()
            if depth != currentDepth:
                currentDepth = depth
                result.append(node.val)

            if node.right:
                queue.append((depth + 1, node.right))
            if node.left:
                queue.append((depth + 1, node.left))

        return result

sol = Solution()
sol.rightSideView(TreeNode(1,
    TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)),
)) # [1,3,4]

sol.rightSideView(TreeNode(1,
    TreeNode(2, TreeNode(4, TreeNode(5))), TreeNode(3),
)) # [1,3,4,5]

sol.rightSideView(TreeNode(1,
    None, TreeNode(3),
)) # [1,3]