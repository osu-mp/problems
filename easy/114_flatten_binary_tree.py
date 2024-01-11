"""
Runtime
42
ms
Beats
64.90%
of users with Python3
Memory
17.62
MB
Beats
33.10%
of users with Python3
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root:
                return None
            left_tail = dfs(root.left)
            right_tail = dfs(root.right)

            if left_tail:
                # left_tail.right = root.right
                left_tail.right, root.right, root.left = root.right, root.left, None

            last = right_tail or left_tail or root
            return last

        dfs(root)
        