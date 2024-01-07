import unittest

class Solution:
    """
    Runtime
Details
35ms
Beats 94.28%of users with Python3
Memory
Details
17.34MB
Beats 29.87%of users with Python3
    """
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        memo = [False] * (len(s)  + 1)
        memo[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i : i + len(word)] == word:
                    memo[i] = memo[i + len(word)]
                if memo[i]:
                    break

        return memo[0]
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        s = "leetcode"
        wordDict = ["leet","code"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

        s = "applepenapple"
        wordDict = ["apple","pen"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

        s = "catsandog"
        wordDict = ["cats","dog","sand","and","cat"]
        self.assertFalse(self.solution.wordBreak(s, wordDict))


if __name__ == '__main__':
    unittest.main()