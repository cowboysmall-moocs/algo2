import unittest

from week5.tsp1 import encode, decode, generate_subsets, generate_grouped_subsets


class TestTSP(unittest.TestCase):

    def test_endoce_decode(self):
        self.assertEqual(encode([0], 24), 1)
        self.assertEqual(decode(1), set([0]))

        self.assertEqual(encode([1, 3, 5], 24), 42)
        self.assertEqual(decode(42), set([1, 3, 5]))

        self.assertEqual(encode([1, 3, 5], 24), 42)
        self.assertEqual(decode(42), set([1, 3, 5]))

        self.assertEqual(encode([23], 24), 8388608)
        self.assertEqual(decode(8388608), set([23]))


    def test_generate_subsets(self):
        self.assertEqual(generate_subsets(2, 0), [0])
        self.assertEqual(generate_subsets(2, 1), [1, 2])
        self.assertEqual(generate_subsets(2, 2), [3])

        self.assertEqual(generate_grouped_subsets(2)[0], [0])
        self.assertEqual(generate_grouped_subsets(2)[1], [1, 2])
        self.assertEqual(generate_grouped_subsets(2)[2], [3])

