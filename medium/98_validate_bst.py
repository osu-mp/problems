"""
Runtime
38
ms
Beats
88.67%
of users with Python3
Memory
18.47
MB
Beats
93.87%
of users with Python3
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def node_valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False

            return (node_valid(node.left, left, node.val) and
                    node_valid(node.right, node.val, right))

        return node_valid(root, float("-inf"), float("inf"))  
        