# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: return

        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next

            if not fast or not fast.next:
                slow.next = slow.next.next
                break
            slow = slow.next
        return head

sol = Solution()
sol.deleteMiddle(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
sol.deleteMiddle(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
sol.deleteMiddle(ListNode(2, ListNode(1)))