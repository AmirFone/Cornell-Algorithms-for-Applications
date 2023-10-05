import unittest
import sys
sys.path.append("..")

from problem_5.p5 import cookies_distrubution_map

class TestProblem5(unittest.TestCase):
    ### Public tests
    def test_correctness_public_n2_split(self):
        """Public test #1 n = 2"""
        route = cookies_distrubution_map([(1,2), (2, 1)])
        self.assertEqual({((1,1), (1,2)), ((1,1), (2,1))}, set(route))

    def test_correctness_public_n2_sequential(self):
        """Public test #2 n = 2"""
        route = cookies_distrubution_map([(1,2), (1, 5)])
        self.assertEqual({((1,1), (1,2)), ((1,2), (1,5))}, set(route))

    def test_correctness_public_n3_tie(self):
        """Public test n = 3"""
        route = cookies_distrubution_map([(1,2), (2, 1), (2, 2)])
        self.assertTrue({((1,1), (1,2)), ((1,1), (2,1)), ((1,2), (2, 2))} == set(route) or {((1,1), (1,2)), ((1,1), (2,1)), ((2,1), (2, 2))} == set(route))

    def test_correctness_public_n4_sequential(self):
        """Public test #1 n = 4"""
        route = cookies_distrubution_map([(2, 2), (3, 3), (4, 4), (5, 5)])
        self.assertEqual({((1,1), (2,2)), ((2,2), (3,3)), ((3,3), (4,4)), ((4,4), (5,5))}, set(route))

    def test_correctness_public_n4_split(self):
        """Public test #2 n = 4"""
        route = cookies_distrubution_map([(1, 5), (2, 5), (1, 7), (6, 1)])
        self.assertEqual({((1,1), (6, 1)), ((1,1), (1,5)), ((1,5), (2,5)), ((1,5), (1,7))}, set(route))

    def test_correctess_public_n6(self):
        """Public test n = 6"""
        route = cookies_distrubution_map([(1,4), (5, 1), (5, 5), (5, 4), (3, 2), (6, 4)])
        self.assertEqual({((1,1), (3, 2)), ((3,2), (5,1)), 
                          ((1,1), (1,4)), ((5,4), (5,5)), 
                          ((5,4), (6,4)), ((5,1), (5,4))}, set(route))

if __name__ == '__main__':
    unittest.main()