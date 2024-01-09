"""
Runtime
Details
38ms
Beats 70.62%of users with Python3
Memory
Details
17.27MB
Beats 26.12%of users with Python3
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        two pointers, keep a gap of n between them
        start at head, advance trail until it is n + 1 between
            then advance both in step until trail hits end
            then first pointer skips next number

        edges:
            no nodes
            remove head
            last element

        """
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0  and right:
            right = right.next
            n -= 1
    
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next
        