# type: ignore

"""
Problem link: https://leetcode.com/problems/linked-list-cycle/

Idea 1: HashSet

Time complexity: O(N)

Space Complexity: O(N)

Idea 2: Modify Linked List to point to visitedNode

Time complexity: O(N)

Space Complexity: O(1)
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visitedNode = ListNode(None)

        while head != None:
            if head == visitedNode:
                return True
            head.next, head = visitedNode, head.next
        return False

sol = Solution()
node0 = ListNode(3)
node1 = ListNode(2)
node2 = ListNode(0)
node3 = ListNode(-4)
node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node1
sol.hasCycle(node0)