"""
Problem: https://leetcode.com/problems/balance-a-binary-search-tree

Idea: Traverse inorder to build a sorted array
The middle of this array is the root. Its left and right is the root of left part and right part

Time: O(N)
Space: O(N)
"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []

        def inorder(node: Optional[TreeNode]):
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        inorder(root)

        def build(left, right: int) -> Optional[TreeNode]:
            if left >= right:
                return

            mid = (right + left) // 2
            root = TreeNode(arr[mid])

            if left == mid - 1:
                root.left = TreeNode(arr[left])
            else:
                root.left = build(left, mid - 1)
            
            if mid == right - 1:
                root.right = TreeNode(arr[right])
            else:
                root.right = build(mid + 1, right)
            return root

        root = build(0, len(arr) - 1)
        return root

sol = Solution()
sol.balanceBST(TreeNode(14, TreeNode(9, TreeNode(2), TreeNode(13)) , TreeNode(16)))
sol.balanceBST(TreeNode(1, right=TreeNode(2, right=TreeNode(3, right=TreeNode(4)))))
sol.balanceBST(TreeNode(2, TreeNode(1), TreeNode(3)))
