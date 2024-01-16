"""
Runtime
65
ms
Beats
67.35%
of users with Python3
Memory
22.72
MB
Beats
63.28%
of users with Python3
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        count = 1
        if root.left:
            count += self.countNodes(root.left)
        if root.right:
            count += self.countNodes(root.right)

        return count