import unittest
from p3_b import local_search_2opt


class TestProblem1(unittest.TestCase):
  def test_correctness_public_a1(self):
    """Public test """
    cost_matrix = [
      [float('inf'), 3, 5],
      [3, float('inf'), 7],
      [5, 7, float('inf')]]
    
    self.assertEqual(local_search_2opt(cost_matrix, (2, 3, 1)),
                     (2, 1, 3))

if __name__ == '__main__':
  unittest.main()