import collections
import unittest

class Solution:
    """
    Runtime
Details
66ms
Beats 48.42%of users with Python3
Memory
Details
17.36MB
Beats 28.49%of users with Python3
    """
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = collections.defaultdict(int)
        for letter in magazine:
            letters[letter] += 1

        for letter in ransomNote:
            if letters[letter] > 0:
                letters[letter] -= 1
            else:
                return False
        return True
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        ransomNote = "a"
        magazine = "b"
        self.assertFalse(self.solution.canConstruct(ransomNote, magazine))

        ransomNote = "aa"
        magazine = "ab"
        self.assertFalse(self.solution.canConstruct(ransomNote, magazine))

        ransomNote = "aa"
        magazine = "aab"
        self.assertTrue(self.solution.canConstruct(ransomNote, magazine))

if __name__ == '__main__':
    unittest.main()
