from collections import defaultdict
import unittest

"""
Runtime
39
ms
Beats
96.14%
of users with Python3
Memory
16.94
MB
Beats
61.11%
of users with Python3
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        chars = defaultdict(int)
        for char in s:
            chars[char] += 1

        for char in t:
            chars[char] -= 1
            if chars[char] < 0:
                return False
        
        for char in chars:
            if chars[char] != 0:
                return False
        
        return True
        
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        s = "anagram"
        t = "nagaram"
        self.assertTrue(self.solution.isAnagram(s, t))

        s = "rat"
        t = "car"
        self.assertFalse(self.solution.isAnagram(s, t))

        s = "rat"
        t = "ratr"
        self.assertFalse(self.solution.isAnagram(s, t))
        
if __name__ == '__main__':
    unittest.main()