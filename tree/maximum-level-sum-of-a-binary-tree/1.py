# type: ignore
"""
Problem: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree
Idea: BFS with a queue
Time: O(N)
Space: O(2^d) with d is tree depth
"""

# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans = 1
        lastLevel = 0
        maxSum = root.val
        currSum = root.val
        q = deque()
        q.append((root, 1))

        while q:
            node, level = q.popleft()
            if level > lastLevel:
                if currSum > maxSum:
                    ans = lastLevel
                    maxSum = currSum
                lastLevel = level
                currSum = 0

            currSum += node.val
            if node.right:
                q.append((node.right, level + 1))
            if node.left:
                q.append((node.left, level + 1))

        if currSum > maxSum:
            ans = lastLevel
        
        return ans

sol = Solution()
sol.maxLevelSum(TreeNode(
    63909,
    TreeNode(
        43838,
        TreeNode(
            -31714,
            TreeNode(75152, None, TreeNode(-83674)),
            TreeNode(-14750)
        ),
        TreeNode(
            -99701,
            TreeNode(-12671, TreeNode(-83490), None),
            TreeNode(60405, TreeNode(-49913), TreeNode(86188))
        )
    ),
    TreeNode(
        4549,
        TreeNode(
            -96320,
            None,
            TreeNode(
                29388,
                TreeNode(
                    84455,
                    TreeNode(-36061, TreeNode(-75550), None),
                    TreeNode(91438)
                ),
                None
            )
        ),
        TreeNode(88666)
    )
))
sol.maxLevelSum(
    TreeNode(1,
        TreeNode(7, TreeNode(7), TreeNode(-8)),
        TreeNode(0)
))
