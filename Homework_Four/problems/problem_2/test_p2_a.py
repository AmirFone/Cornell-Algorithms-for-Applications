import unittest
import p2_a


class TestProblem1(unittest.TestCase):
  def test_correctness_public_a1(self):
    """Public test """
    boxes = [[4,8],[2,8]]
    packages = [2,3,5]
    self.assertEqual(p2_a.linear_search(packages, boxes), 6)

  def test_correctness_public_a2(self):
    """Public test """
    boxes = [[1,4],[2,3],[3,4]]
    packages = [2,3,5]
    self.assertEqual(p2_a.linear_search(packages, boxes), -1)

  def test_correctness_public_a3(self):
    """Public test """
    boxes = [[12],[11,9],[10,5,14]]
    packages = [3,5,8,10,11,12]
    self.assertEqual(p2_a.linear_search(packages, boxes), 9)
    


if __name__ == '__main__':
  unittest.main()