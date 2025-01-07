# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy is to
        # avoid edge case of first step
        # keep the first node why result keep getting replaced by new node
        result = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next
            result = result.next
        
        if list1 or list2:
            result.next = list1 if list1 else list2

        return dummy.next

solution = Solution()
solution.mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4))))
solution.mergeTwoLists(ListNode(1, ListNode(-1, ListNode(4))), ListNode(1))