import collections
import unittest

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = collections.defaultdict(list)
        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1

            result[tuple(count)].append(word)

        return list(result.values())
    
    def groupAnagrams_orig(self, strs: list[str]) -> list[list[str]]:
        groups = collections.defaultdict(list)
        for word in strs:
            word_dict = collections.defaultdict(int)
            for char in word:
                word_dict[char] += 1
            
            dict_str = '{' + ', '.join(f"'{key}': {value}" for key, value in sorted(word_dict.items())) + '}'
            groups[dict_str].append(word)

        return list(groups.values())
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        expected = [["bat"],["nat","tan"],["ate","eat","tea"]]
        self.assertEqual(self.solution.groupAnagrams(strs), expected)

        strs = [""]
        expected = [[""]]
        self.assertEqual(self.solution.groupAnagrams(strs), expected)
        
        strs = ["a"]
        expected = [["a"]]
        self.assertEqual(self.solution.groupAnagrams(strs), expected)
        
        
if __name__ == '__main__':
    unittest.main()