from collections import defaultdict
import unittest

class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = defaultdict(lambda: 0)
        close_map = {')': '(', ']': '[', '}': '{'}
        open_stack = []
        for char in s:
            if char in ['(', '[', '{']:
                open_stack.append(char)
            elif char in [')', ']', '}']:
                if len(open_stack) <= 0:
                    return False
                close_char = close_map[char]
                expected = open_stack.pop()
                if close_char != expected:
                    return False
        
        return len(open_stack) == 0
        

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        self.assertTrue(self.solution.isValid("()"))
        self.assertTrue(self.solution.isValid("()[]{}"))
        self.assertFalse(self.solution.isValid("(]"))
        self.assertFalse(self.solution.isValid("([)]"))
        

if __name__ == '__main__':
    unittest.main()