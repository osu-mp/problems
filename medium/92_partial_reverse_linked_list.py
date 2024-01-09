"""
Runtime
Details
36ms
Beats 72.43%of users with Python3
Memory
Details
17.38MB
Beats 30.59%of users with Python3
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # if left == right:
        #     return head

        dummy = ListNode(0, head)
        left_prev = dummy
        curr = head

        # go until the left node
        for i in range(left - 1):
            left_prev = curr
            curr = curr.next
        
        # reverse every node in between left and right
        prev = None
        for i in range(right - left + 1):
            tmp_next = curr.next
            curr.next = prev
            prev = curr
            curr = tmp_next
        
        # update edge pointers
        left_prev.next.next = curr
        left_prev.next = prev

        return dummy.next
        