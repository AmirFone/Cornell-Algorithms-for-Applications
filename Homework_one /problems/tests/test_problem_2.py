import unittest
import sys
sys.path.append("..")

from problem_2.p2 import interval_covering

class TestProblem2(unittest.TestCase):
    ### Public tests
    def test_cover_all(self):
        """Public test #1 for interval cover"""
        cover = interval_covering(4, [[2, 3], [3, 4], [0, 1], [1, 2]])
        # print(f"expected: {set(tuple(pair) for pair in cover), {(0, 1), (1, 2), (2, 3), (3, 4)}}")
        self.assertEqual(set(tuple(pair) for pair in cover), {(0, 1), (1, 2), (2, 3), (3, 4)})

    def test_cover_size_1(self):
        """Public test #2 for interval cover"""
        cover = interval_covering(6, [[0, 2], [1, 6], [0, 6], [3, 5]])
        # print(f"expected: {set(tuple(pair) for pair in cover), {(0,6)}}")
        self.assertEqual(set(tuple(pair) for pair in cover), {(0,6)})

    def test_cover_size_2(self):
        """Public test #3 for interval cover"""
        cover = interval_covering(6, [[3, 6], [2, 4], [0, 3]])

        # print(F"expected: {set(tuple(pair) for pair in cover), {(3, 6), (0, 3)}}")
        self.assertEqual(set(tuple(pair) for pair in cover), {(3, 6), (0, 3)})

    def test_cover_size_3(self):
        """Public test #4 for interval cover"""
        cover = interval_covering(6, [[0, 2], [0, 1], [2, 3], [2, 4], [4, 6]])
        # print(f"expected: {set(tuple(pair) for pair in cover), {(4, 6), (0, 2), (2, 4)}}")
        self.assertEqual(set(tuple(pair) for pair in cover), {(4, 6), (0, 2), (2, 4)})

if __name__ == '__main__':
    unittest.main()