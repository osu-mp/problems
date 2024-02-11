import unittest

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        i = m + n - 1
        while p2 >=0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
            i -= 1
                
                
    def merge_long(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        i = m + n - 1
        while p1 >=0 and p2 >= 0:
            val1 = nums1[p1]
            val2 = nums2[p2]
            if val1 > val2:
                nums1[i] = val1
                p1 -= 1
            else:
                nums1[i] = val2
                p2 -= 1
            i -=1

        while p1 >= 0:
            nums1[i] = nums1[p1]
            p1 -= 1
            i -= 1
        while p2 >= 0:
            nums1[i] = nums2[p2]
            p2 -= 1
            i -= 1

            
    
    def merge_old(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while i < m:#  and j < n:
            if j >= n:
                break
            print(f"loop {i=}, {j=}, {nums1[i]=}, {nums2[j]=}")
            if nums1[i] <= nums2[j]:
                i += 1
                print("  case 1")
            else:
                nums1[i], nums2[j] = nums2[j], nums1[i]
                j += 1
                print("   case 2")
                i += 1

            print(f"{nums1=}")
            print(f"{nums2=}]\n\n")
        

        for blah in range(n):
            nums1[i] = nums2[blah]
            i += 1

        print(f"{nums1=}")
        print(f"{nums2=}")
            
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        expected = [1,2,2,3,5,6]
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)
        nums1 = [1]; m = 1; nums2 = []; n = 0
        expected = [1]        
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)
        nums1 = [0]; m = 0; nums2 = [1]; n = 1
        expected = [1]        
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)
        
    def test_hidden(self):
        nums1 = [1,2,3,0,0,0]; m = 3; nums2 = [2, 5, 6]; n = 3
        expected = [1, 2, 2, 3, 5, 6]        
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)

        nums1 = [4,0,0,0,0,0]; m = 1; nums2 = [1, 2, 3, 5, 6]; n = 5
        expected = [1, 2, 3, 4, 5, 6]        
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)

        nums1 = [2, 0]; m = 1; nums2 = [1]; n = 1
        expected = [1, 2]        
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)
        

if __name__ == '__main__':
    unittest.main()
