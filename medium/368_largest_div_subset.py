import unittest

class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        cache = {}
        blah = set()
        

        def dfs(i):
            if i == len(nums):
                return []
            if i in cache:
                return cache[i]
            
            result = [nums[i]]
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    tmp = [nums[i]] + dfs(j)
                    if len(tmp) > len(result):
                        result = tmp
            cache[i] = result
            return result
        
        result = []
        for i in range(len(nums)):
            tmp = dfs(i)
            if len(tmp) > len(result):
                result = tmp
    
        return result
    
    def largestDivisibleSubset_orig(self, nums: list[int]) -> list[int]:
        nums.sort()
        cache = {}

        def dfs(i, prev):
            if i == len(nums):
                return []
            if (i, prev) in cache:
                return cache[(i, prev)]
            
            result = dfs(i + 1, prev)
            if nums[i] % prev == 0:
                tmp = [nums[i]] + dfs(i + 1, nums[i])
                result = tmp if len(tmp) > len(result) else result

            cache[(i, prev)] = result
            return result
        return dfs(0, 1)