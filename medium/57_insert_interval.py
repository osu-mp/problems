import unittest

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])

        result.append(newInterval)
        return result


        # new_intervals = []
        # for interval in intervals:
        #     if interval[0] < newInterval[0] < interval[1] or interval[0] < newInterval[1] < interval[1]:
        #         interval[0] = min(interval[0], newInterval[1])
        #         interval[1] = max(interval[1], newInterval[1])

        #         if interval[0] < newInterval[0] < interval[1]:
        #             ass
        #     #     pass
        #     # else:
        #     new_intervals.append(interval)
        # return new_intervals
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        intervals = [[1,3],[6,9]]
        newInterval = [2,5]
        Output = [[1,5],[6,9]]
        self.assertEqual(self.solution.insert(intervals, newInterval), Output)

        intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        newInterval = [4,8]
        Output =[[1,2],[3,10],[12,16]]
        self.assertEqual(self.solution.insert(intervals, newInterval), Output)        
        
if __name__ == '__main__':
    unittest.main()