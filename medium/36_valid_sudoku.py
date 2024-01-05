import collections
import numpy as np
import unittest

class Solution:
    """
    Faster using hashset than multiple np arrays
    Runtime
Details
93ms
Beats 87.07%of users with Python3
Memory
Details
17.16MB
Beats 27.58%of users with Python3
    """
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        subs = collections.defaultdict(set) # key = row // 3, col == 3

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if (board[row][col] in rows[row] or
                    board[row][col] in cols[col]  or
                    board[row][col] in subs[(row // 3, col // 3)]):
                    return False
                
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                subs[(row // 3, col // 3)].add(board[row][col])
        return True
    
    """
    Runtime
Details
189ms
Beats 5.12%of users with Python3
Memory
Details
35.72MB
Beats 6.57%of users with Python3
    """
    def isValidSudoku_slow(self, board: list[list[str]]) -> bool:
        np_array = np.array(board)
        # check rows
        for row in np_array:
            if self.has_duplicates(row):
                # print(f"duplicates in {row=}")
                return False
        # check cols
        for col in np_array.T:
            if self.has_duplicates(col):
                # print(f"duplicates in {col=}")
                return False
        # check sub-boxes
        for i in range(0, 9, 3):
             for j in range(0, 9, 3):
                 sub = np_array[i:i+3, j:j+3]
                 sub = sub.reshape(-1)
                #  print(f"{sub=}")
                 if self.has_duplicates(sub):
                    # print(f"duplicates in {sub=}")
                    return False
                 
        return True
    
    def has_duplicates(self, arr):
        num_set = set()
        for value in arr:
            if value == '.':
                pass
            elif value in num_set:
                return True
            num_set.add(value)
        return False
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        board = [["5","3",".",".","7",".",".",".","."]
,[".",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
        self.assertTrue(self.solution.isValidSudoku(board))

        board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
        self.assertFalse(self.solution.isValidSudoku(board))


        
if __name__ == '__main__':
    unittest.main()
