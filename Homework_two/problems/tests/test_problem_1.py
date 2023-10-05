import unittest
import sys
sys.path.append("..")

from problem_1.p1_a import maxsum_list
from problem_1.p1_b import maxsum_tree

class TestProblem1(unittest.TestCase):
    ### Public tests for 1a
    def test_correctness_public_a1(self):
        """Public test for n = 2"""
        self.assertEqual(maxsum_list([1,2]), 2)

    def test_correctness_public_a2(self):
        """Public test #1 for n = 3"""
        self.assertEqual(maxsum_list([1,2,3]), 4)

    def test_correctness_public_a3(self):
        """Public test #2 for n = 4"""
        self.assertEqual(maxsum_list([1,2,6,4]), 7)

    def test_correctness_public_a4(self):
        """Public test #2 for n = 4"""
        self.assertEqual(maxsum_list([10,1,1,10]), 20)

    def test_correctness_public_a5(self):
        """Public test #2 for n = 4"""
        self.assertEqual(maxsum_list([10,1,1,1,10]), 21)

    ### Public tests for 1b
    def test_correctness_public_b1(self):
        """Public test for n = 2"""
        self.assertEqual(maxsum_tree(
            {
                0: 1,
                1: 2,
                2: 3,
                3: 4,
            },
            {
                0: [1],
                1: [2],
                2: [3],
                3: [],
            },
        ), 6)

    def test_correctness_public_b2(self):
        """Public test for n = 2"""
        self.assertEqual(maxsum_tree(
            {
                0: 1,
                1: 2,
                2: 3,
                3: 4,
            },
            {
                0: [1,2],
                1: [3],
                2: [],
                3: [],
            },
        ), 7)

if __name__ == '__main__':
    unittest.main()
