import unittest

"""
Runtime
29
ms
Beats
97.75%
of users with Python3
Memory
16.64
MB
Beats
60.03%
of users with Python3
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: [ListNode], k: int) -> [ListNode]:
        if not head or k == 0:
            return head
        
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        k = k % length
        print(f"{length=}, {k=}")
        if k == 0:
            return head
        
        cur = head
        for i in range(length - k - 1):
            cur = cur.next
        new_head = cur.next
        cur.next = None
        tail.next = head
        return new_head
    
        # dummy = ListNode(0, head)
        # behind = 0
        # node = head
        # while node and behind < k:
        #     behind += 1
        #     node = node.next
        
        # new_head = node
        # last = node
        # while node:
        #     last = node
        #     node = node.next
        # last.next = none # new_head
        # return new_head

if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode (4))))
    solution = Solution()
    new_head = solution.rotateRight(head, 2)
    while new_head:
        print(f"{new_head.val}")
        new_head = new_head.next
    