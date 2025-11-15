# type: ignore
"""
Idea: Use a deque, traverse and append everything
After reaching the end, pop and popleft until deque empty

Time:
Space:
"""

from typing import Deque, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        queue = Deque()
        dummyHead = head

        while head is not None:
            queue.append(head)
            head = head.next

        tail = None

        while len(queue) > 0:
            head = queue.popleft()
            if tail is not None:
                tail.next = head

            if len(queue) == 0:
                head.next = None
                break

            tail = queue.pop()
            head.next = tail
            if len(queue) == 0:
                tail.next = None
        
        return dummyHead

sol = Solution()
sol.reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
sol.reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
sol.reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
sol.reorderList(ListNode(1))
sol.reorderList(ListNode(1, ListNode(2)))
