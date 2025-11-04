# type: ignore
"""
Idea:
Step 1: Reverse 2 lists
Step 2: Add and reverse 2 lists at the same time

Time: O(N)

Space: O(N)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        len1 = 0
        while l1 != None:
            len1 += 1
            nxt = l1.next
            l1.next = prev
            prev = l1
            l1 = nxt
            if l1 == None:
                l1 = prev
                break

        prev = None
        len2 = 0
        while l2 != None:
            len2 += 1
            nxt = l2.next
            l2.next = prev
            prev = l2
            l2 = nxt
            if l2 == None:
                l2 = prev
                break
        
        long = l1 if len1 > len2 else l2
        short = l1 if len1 <= len2 else l2
        prev = None
        result = 0
        while long != None or short != None:
            if long != None:
                result += long.val
            if short != None:
                result += short.val
            long.val = result % 10
            result = 1 if result >= 10 else 0
            nxt = long.next
            long.next = prev
            prev = long
            long = nxt

            if short != None:
                short = short.next
        
        if result == 1:
            prev = ListNode(1, prev)
        return prev

sol = Solution()
sol.addTwoNumbers(ListNode(9, ListNode(9, ListNode(9, ListNode(9)))), ListNode(9, ListNode(9, ListNode(9))))
sol.addTwoNumbers(ListNode(7, ListNode(2, ListNode(4, ListNode(3)))), ListNode(5, ListNode(6, ListNode(4))))
