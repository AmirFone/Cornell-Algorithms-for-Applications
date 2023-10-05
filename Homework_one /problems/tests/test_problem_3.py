import unittest
import sys
sys.path.append("..")

from problem_3.p3_a import number_of_large_inversions_3a
from problem_3.p3_b import number_of_large_inversions_3b

class TestProblem3(unittest.TestCase):

    ### Public tests for 3a

    def test_correctness_public_a_n4_1(self):
        """Public test # 1 for n = 4"""
        num_inversions = number_of_large_inversions_3a("input/test_p3_public_n4_1.txt", 1)
        self.assertEqual(num_inversions, 2)

    def test_correctness_public_a_n4_2(self):
        """Public test # 2 for n = 4"""
        num_inversions = number_of_large_inversions_3a("input/test_p3_public_n4_1.txt", 2)
        self.assertEqual(num_inversions, 1)

    def test_correctness_public_a_n4_3(self):
        """Public test # 3 for n = 4"""
        num_inversions = number_of_large_inversions_3a("input/test_p3_public_n4_2.txt", 1)
        self.assertEqual(num_inversions, 2)

    def test_correctness_public_a_n4_4(self):
        """Public test # 4 for n = 4"""
        num_inversions = number_of_large_inversions_3a("input/test_p3_public_n4_2.txt", 2)
        self.assertEqual(num_inversions, 0)

    def test_correctness_public_a_n8_1(self):
        """Public test # 1 for n = 8"""
        num_inversions = number_of_large_inversions_3a("input/test_p3_public_n8.txt", 1)
        self.assertEqual(num_inversions, 9)

    def test_correctness_public_a_n8_2(self):
        """Public test # 2 for n = 8"""
        num_inversions = number_of_large_inversions_3a("input/test_p3_public_n8.txt", 2)
        self.assertEqual(num_inversions, 7)

    def test_correctness_public_a_n8_3(self):
        """Public test # 3 for n = 8"""
        num_inversions = number_of_large_inversions_3a("input/test_p3_public_n8.txt", 3)
        self.assertEqual(num_inversions, 5)

    ## Public tests for 3b
    def test_correctness_public_b_n4_1(self):
        """Public test # 1 for n = 4"""
        num_inversions = number_of_large_inversions_3b("input/test_p3_public_n4_1.txt", 1)
        self.assertEqual(num_inversions, 2)

    def test_correctness_public_b_n4_2(self):
        """Public test # 2 for n = 4"""
        num_inversions = number_of_large_inversions_3b("input/test_p3_public_n4_1.txt", 2)
        self.assertEqual(num_inversions, 1)

    def test_correctness_public_b_n4_3(self):
        """Public test # 3 for n = 4"""
        num_inversions = number_of_large_inversions_3b("input/test_p3_public_n4_2.txt", 1)
        self.assertEqual(num_inversions, 2)

    def test_correctness_public_b_n4_4(self):
        """Public test # 4 for n = 4"""
        num_inversions = number_of_large_inversions_3b("input/test_p3_public_n4_2.txt", 2)
        self.assertEqual(num_inversions, 0)

    def test_correctness_public_b_n8_1(self):
        """Public test # 1 for n = 8"""
        num_inversions = number_of_large_inversions_3b("input/test_p3_public_n8.txt", 1)
        self.assertEqual(num_inversions, 9)

    def test_correctness_public_b_n8_2(self):
        """Public test # 2 for n = 8"""
        num_inversions = number_of_large_inversions_3b("input/test_p3_public_n8.txt", 2)
        self.assertEqual(num_inversions, 7)

    def test_correctness_public_b_n8_3(self):
        """Public test # 3 for n = 8"""
        num_inversions = number_of_large_inversions_3b("input/test_p3_public_n8.txt", 3)
        self.assertEqual(num_inversions, 5)

if __name__ == '__main__':
    unittest.main()