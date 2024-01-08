"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    """
    Runtime
Details
39ms
Beats 76.37%of users with Python3
Memory
Details
18.04MB
Beats 33.47%of users with Python3
    """
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Iterate through the list once, creating a hashmap of each address of each node (value = spot in line)
            Create new list using values
        Second iteration, 
        """
        old_to_copy = {None: None}

        curr = head
        while curr:
            new_node = Node(curr.val)
            old_to_copy[curr] = new_node

            curr = curr.next

        curr = head
        while curr:
            copy = old_to_copy[curr]
            copy.next = old_to_copy[curr.next]
            copy.random = old_to_copy[curr.random]

            curr = curr.next

        return old_to_copy[head]

        