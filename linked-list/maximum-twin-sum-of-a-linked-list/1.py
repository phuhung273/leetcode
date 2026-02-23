# type: ignore
"""
Problem: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list
Idea: Fast and slow pointer
Slow pointer traverse and reverse the list
When fast pointer reach the end, stop reversing with slow pointer
Use 2 pointers to traverse outward and compare
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
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        reversed = None

        while fast:
            fast = fast.next.next
            nxt = slow.next
            slow.next = reversed
            reversed = slow
            slow = nxt

        ans = 0
        while slow:
            ans = max(ans, slow.val + reversed.val)
            slow = slow.next
            reversed = reversed.next
        return ans

sol = Solution()
sol.pairSum(ListNode(5, ListNode(4, ListNode(2, ListNode(1)))))
sol.pairSum(ListNode(4, ListNode(2, ListNode(2, ListNode(3)))))
sol.pairSum(ListNode(1, ListNode(100000)))
