import collections
import unittest

"""
Runtime
27
ms
Beats
96.42%
of users with Python3
Memory
16.56
MB
Beats
62.08%
of users with Python3
"""
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        """
        at each node, find mutations that are off by one in bank
        if end gene, done
        if not, add to queue the unvisited
        """
        bank = set(bank)
        if endGene not in bank:
            return -1
        
        def getOneCharMutations(gene):
            found = []
            for mutated in bank:
                diff = sum(char1 != char2 for char1, char2 in zip(gene, mutated))
                if diff == 1:
                    found.append(mutated)
            return found
        
        visited = set()
        visited.add(startGene)
        queue = collections.deque()
        queue.append((startGene, 0))
        while queue:
            gene, level = queue.popleft()
            visited.add(gene)
            if gene == endGene:
                return level
            
            possible = getOneCharMutations(gene)
            for mutated in possible:
                if mutated not in visited:
                    queue.append((mutated, level + 1))

        return -1
        
        

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        startGene = "AACCGGTT"
        endGene = "AACCGGTA"
        bank = ["AACCGGTA"]
        self.assertEqual(self.solution.minMutation(startGene, endGene, bank), 1)

        startGene = "AACCGGTT"
        endGene = "AAACGGTA"
        bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
        self.assertEqual(self.solution.minMutation(startGene, endGene, bank), 2)
        
if __name__ == '__main__':
    unittest.main()