import unittest
import p1_b


class TestProblem1(unittest.TestCase):
  def test_correctness_public_a1(self):
    """Public test """
    a = [1, 2]
    b = [3, 5]
    w = 3
    p = 100
    stream = [10, 11, 10]
    true_solution = [[0, 2, 1], [1, 2, 0]]
    self.assertListEqual(
      p1_b.count_min_sketch(a, b, w, p, stream),
      true_solution)

  def test_correctness_public_a2(self):
    """Public test """
    a = [2, 3, 4]
    b = [2, 4, 5]
    w = 5
    p = 1000
    stream = range(2, 1000, 3)
    true_solution = [[66, 67, 67, 67, 66], [67, 66, 66, 67, 67], [67, 66, 67, 67, 66]]
    self.assertListEqual(
      p1_b.count_min_sketch(a, b, w, p, stream),
      true_solution)
    


if __name__ == '__main__':
  unittest.main()