import unittest

"""
Runtime
24
ms
Beats
99.45%
of users with Python3
Memory
16.60
MB
Beats
60.28%
of users with Python3
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        final = []
        for dir in dirs:
            if dir in ['/', '.', '']:
                continue
            if dir == '..':
                if final:
                    final.pop()
                continue
            final.append(dir)
            
        return "/" + "/".join(final)
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        path = "/home/"
        expected = "/home"
        self.assertEqual(self.solution.simplifyPath(path), expected)

        path = "/../"
        expected = "/"
        self.assertEqual(self.solution.simplifyPath(path), expected)

        path = "/home//foo/"
        expected = "/home/foo"
        self.assertEqual(self.solution.simplifyPath(path), expected)

if __name__ == '__main__':
    unittest.main()