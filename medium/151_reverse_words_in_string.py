import unittest

"""
Runtime
29
ms
Beats
96.38%
of users with Python3
Memory
17.34
MB
Beats
46.17%
of users with Python3
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        # s = s.strip()
        words = reversed(s.split(" "))
        return " ".join(word for word in words if word)
    

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        s = "the sky is blue"
        expected = "blue is sky the"
        self.assertEqual(self.solution.reverseWords(s), expected)

        s = "  hello world  "
        expected = "world hello"
        self.assertEqual(self.solution.reverseWords(s), expected)

        s = "a good   example"
        expected = "example good a"
        self.assertEqual(self.solution.reverseWords(s), expected)
        
if __name__ == '__main__':
    unittest.main()