import unittest
import sys
sys.path.append("..")


from problem_1.p1_a import is_bipartite
from problem_1.p1_b import maximal_bipartite_match


class TestProblem1(unittest.TestCase):
    ### Public tests for 1a
    def test_correctness_public_a1(self):
        """Public test """
        g_l = {0: [2, 4], 2: [7], 4: [6], 1: [4, 7], 7: [], 3: [6], 6: [], 5: [6]}
        self.assertEqual(is_bipartite(g_l), False)
        # pass

    def test_correctness_public_a2(self):
        """Public test """
        g_l = {0: [1], 1: [3, 6, 7], 3: [4], 6: [7], 7: [8], 2: [4, 6], 4: [8], 8: [], 5: [8]}
        self.assertEqual(is_bipartite(g_l), False)
        # pass

    def test_correctness_public_a3(self):
        """Public test """
        g_l = {0: [2], 2: [], 1: [3], 3: []}
        self.assertEqual(is_bipartite(g_l), True)
        # pass

    def test_correctness_public_a4(self):
        """Public test """
        g_l = {0: [1, 3, 4], 1: [7], 3: [6], 4: [5, 7], 7: [], 2: [3, 6], 6: [], 5: []}
        self.assertEqual(is_bipartite(g_l), False)
        # pass

    def test_correctness_public_a5(self):
        """Public test """
        g_l = {0: [], 1: [4], 4: [], 2: [5], 5: [], 3: [], 6: []}
        self.assertEqual(is_bipartite(g_l), True)
        # pass

    ### Public tests for 1b
    def test_correctness_public_b1(self):
        """Public test """
        g_l = [[0, 1, 0, 1], [1, 1, 1, 1], [0, 0, 0, 1], [0, 0, 1, 1], [0, 0, 1, 1]]
        self.assertEqual(maximal_bipartite_match(g_l), 4)

    def test_correctness_public_b2(self):
        """Public test """
        g_l = [[1, 1, 1, 1], [1, 0, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0]]
        self.assertEqual(maximal_bipartite_match(g_l), 3)
        
    def test_correctness_public_b3(self):
        """Public test """
        g_l = [[0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(maximal_bipartite_match(g_l), 5)
        
    def test_correctness_public_b2(self):
        """Public test """
        g_l = [[0, 0, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0]]
        self.assertEqual(maximal_bipartite_match(g_l), 2)
        
if __name__ == '__main__':
    unittest.main()
