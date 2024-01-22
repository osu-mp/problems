import unittest

"""
Runtime
30
ms
Beats
99.90%
of users with Python3
Memory
18.32
MB
Beats
98.80%
of users with Python3
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        min_diff = float('inf')

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            nonlocal prev, min_diff
            if prev:
                min_diff = min(min_diff, node.val - prev.val)
            prev = node
            dfs(node.right)
        
        dfs(root)
        return min_diff
        