import itertools
import unittest
import p3_a


def _compute_cost(cost_matrix, sequence):
  sum = 0
  for i in range(len(sequence) - 1):
    sum += cost_matrix[sequence[i] - 1][sequence[i+1] - 1]
  return sum


class TestProblem1(unittest.TestCase):
  def test_correctness_public_a1(self):
    """Public test """
    cost_matrix = p3_a.cost_matrix_greedy_approach()
    self.assertEqual(len(cost_matrix), 4)

  def test_correctness_public_a2(self):
    """Public test """
    cost_matrix = p3_a.cost_matrix_greedy_approach()
    self.assertEqual(len(cost_matrix[0]), 4)

  def test_correctness_public_a1(self):
    """Public test """
    cost_matrix = p3_a.cost_matrix_greedy_approach()
    seq_to_cost = {}
    greedy_sol = tuple(p3_a.greedy_solution(cost_matrix))
    for sequence in list(itertools.permutations(list(range(1, 5, 1)), 4)):
      seq_to_cost[sequence] = _compute_cost(cost_matrix, sequence)
    self.assertAlmostEqual(seq_to_cost[greedy_sol], max(seq_to_cost.values()))

if __name__ == '__main__':
  unittest.main()