import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        
        left = 0
        max_len = 0
        
        chars = set()
        chars.add(s[left])
        for right in range(1, len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            max_len = max(max_len, right - left + 1)
       

        return max_len

"""
Runtime
Details
55ms
Beats 81.75%of users with Python3
Memory
Details
17.29MB
Beats 24.23%of users with Python3
"""
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        s = "abcabcbb"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 3)
        s = "bbbbb"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 1)
        s = "pwwkew"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 3)
        
    def test_mind(self):
        s = "abcda"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 4)
        s = "abcdb"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 4)
        s = "abcdabcde"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 5)
        s = ""
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 0)
        s = "x"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 1)
        s = "abcabcdeabcd"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 5)

if __name__ == '__main__':
    unittest.main()
