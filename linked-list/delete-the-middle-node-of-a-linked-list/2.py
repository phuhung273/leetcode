"""
Problem: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list
Idea: Fast and slow pointers
When fast.next.next is None, middle is slow.next
Time: O(N)
Space: O(1)
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        slow = fast = head

        while fast.next and fast.next.next:
            fast = fast.next.next

            if not fast.next:
                break
            slow = slow.next
        
        slow.next = slow.next.next

        return head

sol = Solution()
sol.deleteMiddle(ListNode(2, ListNode(1)))
sol.deleteMiddle(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
sol.deleteMiddle(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
