import re
import unittest

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # This regular expression matches any character that is not alphanumeric
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        left = 0 
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1 
        return True
    """
    Runtime
Details
37ms
Beats 97.25%of users with Python3
Memory
Details
18.97MB
Beats 14.80%of users with Python3
    """
           
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        s = "A man, a plan, a canal: Panama"
        self.assertTrue(self.solution.isPalindrome(s))
        s = "race a car"
        self.assertFalse(self.solution.isPalindrome(s))
        s = " "
        self.assertTrue(self.solution.isPalindrome(s))
        
        

if __name__ == '__main__':
    unittest.main()
