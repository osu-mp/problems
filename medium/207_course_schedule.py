import collections
import unittest

"""
Runtime
92
ms
Beats
68.40%
of users with Python3
Memory
18.50
MB
Beats
77.06%
of users with Python3
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        req_map = collections.defaultdict(set)
        for course, pre in prerequisites:
            req_map[course].add(pre)

        checked = set()

        def dfs(course):
            if course in checked:
                return False
            if not req_map[course]:
                return True
            
            checked.add(course)
            for pre_course in req_map[course]:
                if not dfs(pre_course):
                    return False
                
            checked.remove(course)
            req_map[course] = set()
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
            
        return True
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        numCourses = 2
        prerequisites = [[1,0]]
        self.assertTrue(self.solution.canFinish(numCourses, prerequisites))

        numCourses = 2
        prerequisites = [[1,0],[0,1]]
        self.assertFalse(self.solution.canFinish(numCourses, prerequisites))

        numCourses = 3
        prerequisites = [[1,0], [1, 2]]
        self.assertTrue(self.solution.canFinish(numCourses, prerequisites))

        
if __name__ == '__main__':
    unittest.main()
