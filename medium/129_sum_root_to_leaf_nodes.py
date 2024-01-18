import unittest

"""
Runtime
34
ms
Beats
81.89%
of users with Python3
Memory
17.34
MB
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root) -> int:

        def dfs(node, value):
            if not node:
                return 0
            
            value = value * 10 + node.val
            if node.left:
                value += dfs(node.left, value)
            if not node.left and not node.right:
                return value
            return dfs(node.left, value) + dfs(node.right, value)
        
        return dfs(root, 0)
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(self.solution.sumNumbers(root), 25)

        
if __name__ == '__main__':
    unittest.main()