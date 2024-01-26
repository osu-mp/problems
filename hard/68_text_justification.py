import unittest
"""
Runtime
29
ms
Beats
96.20%
of users with Python3
Memory
16.80
MB
Beats
58.74%
of users with Python3
"""

class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        lines = []
        line = []
        length = 0
        i = 0
        while i < len(words):
            min_width = max(1, len(line) - 1)
            if length + len(line) + len(words[i]) > maxWidth:
                extra_space = maxWidth - length

                spaces = extra_space // min_width
                remainder = extra_space % min_width

                for j in range(min_width):
                    line[j] += " " * spaces
                    if remainder:
                        line[j] += " "
                        remainder -= 1

                lines.append("".join(line))
                line = []
                length = 0

            line.append(words[i])
            length += len(words[i])
            i += 1

        last_line = " ".join(line)
        trail_spaces = maxWidth - len(last_line)
        lines.append(last_line + " " * trail_spaces)

        return lines
        
    def fullJustify_old(self, words: list[str], maxWidth: int) -> list[str]:
        lines = []
        while words:
            size = 0
            line = []
            for word in list(words):
                if len(word) + size < maxWidth:
                    line.append(word)
                    words.remove(word)
                    size += len(word) + 1
                else:
                    break

            if not words or len(line) == 1:
                last = " ".join(line)
                lines.append(last.ljust(maxWidth))
            else:
                spaces = maxWidth - size
                spaces_per = spaces // (len(line) - 1)
                print(f"{spaces_per=}")
                join_str = " " * spaces_per
                lines.append(join_str.join(line))
                print(f"extra spaces {spaces=}")

        return lines

    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        # words = ["justification."]
        # maxWidth = 16
        # expected = ["justification.  "]
        # self.assertEqual(self.solution.fullJustify(words, maxWidth), expected)
        
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        maxWidth = 16
        expected = ["This    is    an",
                    "example  of text",
                    "justification.  "]
        self.assertEqual(self.solution.fullJustify(words, maxWidth), expected)

        words = words = ["What","must","be","acknowledgment","shall","be"]
        maxWidth = 16
        expected = [ "What   must   be",
                      "acknowledgment  ",
                          "shall be        "]
        self.assertEqual(self.solution.fullJustify(words, maxWidth), expected)

        words = words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
        maxWidth = 20
        expected = ["Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "]

        self.assertEqual(self.solution.fullJustify(words, maxWidth), expected)
        
if __name__ == '__main__':
    unittest.main()