import unittest
import sys
sys.path.append("..")


from problem_3.p3_a import find_paths


class TestProblem3(unittest.TestCase):
    ### Public tests for 3a
    def test_correctness_public_a1(self):
        self.assertEqual(find_paths(n = 4, paths = [(1,2), (1,3), (2,3), (3,4), (1,4)]), 2)
        
    def test_correctness_public_a2(self):
        self.assertEqual(find_paths(n = 5, paths = [(1,2), (3,4), (1,5), (2,5)]), 2)
        
    def test_correctness_public_a3(self):
        self.assertEqual(find_paths(n = 12, paths = [(1,4), (1,8), (1,9), (8, 9), (9, 12), (8, 11), (8, 12), (3,4), (3, 12), (1,5), (2,5)]), 3)
        
if __name__ == '__main__':
    unittest.main()
