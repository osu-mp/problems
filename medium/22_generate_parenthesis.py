import unittest

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        strs = []
        stack = []

        def backtrack(num_open, num_close):
            if num_open == num_close == n:
                strs.append("".join(stack))
                return
            if num_open < n:
                stack.append("(")
                backtrack(num_open + 1, num_close)
                stack.pop()

            if num_close < num_open:
                stack.append(")")
                backtrack(num_open, num_close + 1)
                stack.pop()

        backtrack(0, 0)

        return strs
    

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        n = 3
        expected = ["((()))","(()())","(())()","()(())","()()()"]
        self.assertEqual(self.solution.generateParenthesis(n), expected)

        n = 1
        expected = ["()"]
        self.assertEqual(self.solution.generateParenthesis(n), expected)

if __name__ == '__main__':
    unittest.main()

