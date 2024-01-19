import unittest

"""
Runtime
944
ms
Beats
85.00%
of users with Python3
Memory
22.89
MB
Beats
30.83%
of users with Python3
"""

class Solution:   
    """
    This uses the intuition that if we can make it to the end of the loop, that station will loop all the way around.
    Thanks Neetcode for the help: https://www.youtube.com/watch?v=lJwbPZGo05A
    """
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        tank = 0
        station = 0
        for i in range(len(gas)):
            tank += (gas[i] - cost[i])

            if tank < 0:
                tank = 0 
                station = i + 1

        return station
    
    def canCompleteCircuit_slow(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        num_stations = len(gas)
        for station in range(num_stations):
            curr_station = station
            tank = gas[curr_station]
            stations_left = num_stations
            while stations_left > 0:
                tank -= cost[curr_station]
                if tank < 0:
                    break
                curr_station = (curr_station + 1) % num_stations
                tank += gas[curr_station]
                stations_left -= 1
                
            if tank >= 0:
                return station

        return -1
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        gas = [1,2,3,4,5]
        cost = [3,4,5,1,2]
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), 3)

        gas = [2,3,4]
        cost = [3,4,3]
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), -1)

        gas = [5,1,2,3,4]
        cost = [4,4,1,5,1]
        self.assertEqual(self.solution.canCompleteCircuit(gas, cost), 4)

        
if __name__ == '__main__':
    unittest.main()