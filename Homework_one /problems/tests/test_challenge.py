import unittest
import sys
sys.path.append("..")

from challenge.challenge import reference_multiply, karatsuba, fft

class TestChallenge(unittest.TestCase):
    ### Public tests
    def test_correctness_public_n2_reference(self):
        """Public test #1 n = 2"""
        x = [1,0,1]
        y = [1,0,1]
        product = reference_multiply(x, y)
        self.assertEqual([1, 1, 0, 0, 1], product)

    def test_correctness_public_n5_reference(self):
        """Public test #4 n = 5"""
        x = [1,0,1,1,1]
        y = [1,0,1,0,0]
        product = reference_multiply(x, y)
        self.assertEqual([1,1,1,0,0,1,1,0,0], product)
    
    def test_correctness_public_n20_reference(self):
        """Public test #7 n = 20"""
        x = [1,1,0,0,1,1,1,0,0,1,0,0,0,1,1,1,1,1,0,1]
        y = [1,1,1,1,1,1,1,0,0,0,0,1,0,0,1,1,0,0,0,0]
        product = reference_multiply(x, y)
        self.assertEqual([1,1,0,0,1,1,0,0,1,0,1,1,1,0,1,0,1,0,0,0,1,1,1,1,1,0,1,1,0,1,0,0,0,1,1,1,0,0,0,0], product)
    
    def test_correctness_public_n2_karatsuba(self):
        """Public test #2 n = 2"""
        x = [1,0,1]
        y = [1,0,1]
        product = karatsuba(x, y)
        self.assertEqual([1, 1, 0, 0, 1], product)

    def test_correctness_public_n2_fft(self):
        """Public test #3 n = 2"""
        x = [1,0,1]
        y = [1,0,1]
        product = fft(x, y)
        self.assertEqual([1, 1, 0, 0, 1], product)


    def test_correctness_public_n5_karatsuba(self):
        """Public test #5 n = 5"""
        x = [1,0,1,1,1]
        y = [1,0,1,0,0]
        product = karatsuba(x, y)
        self.assertEqual([1,1,1,0,0,1,1,0,0], product)

    def test_correctness_public_n5_fft(self):
        """Public test #6 n = 5"""
        x = [1,0,1,1,1]
        y = [1,0,1,0,0]
        product = fft(x, y)
        self.assertEqual([1,1,1,0,0,1,1,0,0], product)


    def test_correctness_public_n20_karatsuba(self):
        """Public test #8 n = 20"""
        x = [1,1,0,0,1,1,1,0,0,1,0,0,0,1,1,1,1,1,0,1]
        y = [1,1,1,1,1,1,1,0,0,0,0,1,0,0,1,1,0,0,0,0]
        product = karatsuba(x, y)
        self.assertEqual([1,1,0,0,1,1,0,0,1,0,1,1,1,0,1,0,1,0,0,0,1,1,1,1,1,0,1,1,0,1,0,0,0,1,1,1,0,0,0,0], product)

    def test_correctness_public_n20_fft(self):
        """Public test #9 n = 20"""
        x = [1,1,0,0,1,1,1,0,0,1,0,0,0,1,1,1,1,1,0,1]
        y = [1,1,1,1,1,1,1,0,0,0,0,1,0,0,1,1,0,0,0,0]
        product = fft(x, y)
        self.assertEqual([1,1,0,0,1,1,0,0,1,0,1,1,1,0,1,0,1,0,0,0,1,1,1,1,1,0,1,1,0,1,0,0,0,1,1,1,0,0,0,0], product)


if __name__ == '__main__':
    unittest.main()
