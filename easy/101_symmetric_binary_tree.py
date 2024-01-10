import unittest

"""
Runtime
41
ms
Beats
55.53%
of users with Python3
Memory
17.36
MB
Beats
23.42%
of users with Python3
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # return self.isMirror(root, root)
        return self.isMirrorIterative(root)

    # recursive approach
    def isMirror(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True
        
        if (root1 is not None and root2 is not None):
            if root1.val == root2.val:
                return (self.isMirror(root1.left, root2.right) and
                        self.isMirror(root1.right, root2.left))
        return False

    # iterative approach
    def isMirrorIterative(self, root: Optional[TreeNode]) -> bool:
        if root is None: 
            return True
        
        stack = [] 
        stack.append(root.left)
        stack.append(root.right)

        while stack:
            node1 = stack.pop()
            node2 = stack.pop()

            # If both nodes are null, continue the loop
            if not node1 and not node2:
                continue
            
            # If one of the nodes is null, the binary tree is not symmetric
            if not node1 or not node2:
                return False
            
            # If the values of the nodes are not equal, the binary tree is not symmetric
            if node1.val != node2.val:
                return False
            
            # Push the left and right subtrees of the left and right nodes onto the stack in the opposite order
            stack.append(node1.left)
            stack.append(node2.right)
            stack.append(node1.right)
            stack.append(node2.left)

        return True
