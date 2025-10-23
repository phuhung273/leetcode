# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryForward = 0
        dummyNode = head = ListNode()
        while l1 != None or l2 != None:
            if l1 != None:
                carryForward += l1.val
                l1 = l1.next
            if l2 != None:
                carryForward += l2.val
                l2 = l2.next

            head.next = ListNode(carryForward % 10)
            head = head.next
            carryForward = 1 if carryForward >= 10 else 0
        
        if carryForward == 1:
            head.next = ListNode(1)

        return dummyNode.next

sol = Solution()
sol.addTwoNumbers(
    l1 = ListNode(2, ListNode(4, ListNode(3))),
    l2 = ListNode(5, ListNode(6, ListNode(4))),
)

sol.addTwoNumbers(
    l1 = ListNode(9, ListNode(9, ListNode(9))),
    l2 = ListNode(9, ListNode(9)),
)

sol.addTwoNumbers(
    l1 = ListNode(9, ListNode(9)),
    l2 = ListNode(9, ListNode(9, ListNode(9))),
)
