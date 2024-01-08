
class Solution:
    """
    Runtime
Details
44ms
Beats 93.75%of users with Python3
Memory
Details
19.97MB
Beats 81.96%of users with Python3
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # ref: https://www.geeksforgeeks.org/floyds-cycle-finding-algorithm/
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
