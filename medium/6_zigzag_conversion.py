import unittest

"""
Runtime
51
ms
Beats
81.94%
of users with Python3
Memory
17.44
MB
Beats
31.01%
of users with Python3
"""
class Solution:
    """
    D,D,D,U,D,D,D,U
    # down
    for i in range(rows):
        char
    # up
    for i in range(rows-2):
        char

    n = 3
    00..04..08..12
    010305070911
    02..06..10

    n = 4
    00....06
    01..0507
    0204..08
    03....09
    """
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        zigzag = ""
        str_len = len(s)
        for row in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(row, str_len, increment):
                zigzag += s[i]
                diagonal_ind = i + increment - 2 * row
                if (0 < row < numRows - 1) and  (diagonal_ind) < str_len:
                    zigzag += s[diagonal_ind]

        return zigzag
            # first = row
            # print(f"{row=}")
            # for i in range(first, len(s), numRows + 1):
            #     print(f"{i=}, {s[i]=}")
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        s = "PAYPALISHIRING"
        numRows = 3
        expected = "PAHNAPLSIIGYIR"
        self.assertEqual(self.solution.convert(s, numRows), expected)

        s = "PAYPALISHIRING"
        numRows = 4
        expected = "PINALSIGYAHRPI"
        self.assertEqual(self.solution.convert(s, numRows), expected)

        
if __name__ == '__main__':
    unittest.main()
