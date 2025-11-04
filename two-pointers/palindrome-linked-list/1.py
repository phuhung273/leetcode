# type: ignore
"""
Idea 1: Iterate and add element to a queue 
At the end of list, start popping

Time: O(N)

Space: O(N)



Idea 2: Move Slow and fast pointers
Build a reverse list using head
When fast reach the end, move head backward and slow forward to check

Time: O(N)

Space: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        prev = None
        while fast != None and fast.next != None:
            fast = fast.next.next
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        if fast != None:
            slow = slow.next
        
        while slow != None:
            if slow.val != prev.val:
                return False
            slow = slow.next
            prev = prev.next
        
        return True

sol = Solution()
sol.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1)))))
sol.isPalindrome(ListNode(1, ListNode(2, ListNode(2))))
sol.isPalindrome(ListNode(1, ListNode(2, ListNode(3, ListNode(1)))))
sol.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(3)))))
