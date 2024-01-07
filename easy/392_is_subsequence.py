import unittest

class Solution:
    """
    Runtime
Details
33ms
Beats 89.12%of users with Python3
Memory
Details
17.26MB
Beats 30.25%of users with Python3
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        s_i = 0
        len_s = len(s)
        if len_s == 0:
            return True
        for t_i in range(len(t)):
            if s[s_i] == t[t_i]:
                s_i += 1
                if s_i >= len_s:
                    return True
        return False


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        s = "abc"
        t = "ahbgdc"
        self.assertTrue(self.solution.isSubsequence(s, t))
        s = "axc"
        t = "ahbgdc"
        self.assertFalse(self.solution.isSubsequence(s, t))

    def test_extra(self):
        s = "gksrek"
        t = "geeksforgeeks"
        self.assertTrue(self.solution.isSubsequence(s, t))

        s = ""
        t = "ahbgdc"
        self.assertTrue(self.solution.isSubsequence(s, t))
        

if __name__ == '__main__':
    unittest.main()
