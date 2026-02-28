"""
Problem: https://leetcode.com/problems/path-sum-iii
Idea: DFS return a array of sum. Iterate and check array at the same time to build a new array
Time:
Space:
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode]) -> list:
            nonlocal ans

            if not node:
                return []
            if node.val == targetSum:
                ans += 1

            arrLeft = dfs(node.left)
            arrRight = dfs(node.right)
            arr = [node.val]

            def addToArr(src: list):
                nonlocal ans
                for i in src:
                    new = node.val + i
                    if new == targetSum:
                        ans += 1
                    arr.append(new)
            
            addToArr(arrLeft)
            addToArr(arrRight)
            return arr     

        dfs(root)
        return ans

sol = Solution()
sol.pathSum(
    TreeNode(10,
        TreeNode(5,
            TreeNode(3, TreeNode(3), TreeNode(-2)),
            TreeNode(2, None, TreeNode(1))),
        TreeNode(-3, None, TreeNode(11))
    )
    ,8
)
