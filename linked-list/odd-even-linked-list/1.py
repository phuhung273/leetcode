# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        odd, even = head, head.next
        originalEven = even

        while odd and even:
            if odd and odd.next:
                nextOdd = odd.next.next
                odd.next = nextOdd

                if nextOdd:
                    odd = nextOdd
            if even and even.next:
                nextEven = even.next.next
                even.next = nextEven
                even = nextEven
            
            if not nextOdd:
                break
                   
        odd.next = originalEven
        return head

sol = Solution()
sol.oddEvenList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))))
sol.oddEvenList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
sol.oddEvenList(ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7))))))))