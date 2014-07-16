import unittest

from week2.union_find import UnionFind


class TestUnionFind(unittest.TestCase):

    def test_basics(self):
        uf = UnionFind(10)
        uf.union(1, 2)
        uf.union(3, 4)
        uf.union(5, 6)
        uf.union(7, 8)
        uf.union(9, 10)
        self.assertEqual(uf.count(), 5)

        uf.union(2, 5)
        uf.union(3, 8)
        self.assertEqual(uf.count(), 3)

        uf.union(1, 10)
        self.assertEqual(uf.count(), 2)
