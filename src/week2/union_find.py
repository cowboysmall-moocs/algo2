

class UnionFind:

    def __init__(self, count):
        self.union_count = count
        self.data = []
        for i in range(count):
            self.data.append(i + 1)

    def count(self):
        return self.union_count

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        return self.data[p - 1]

    def union(self, p, q):
        p_parent = self.find(p)
        q_parent = self.find(q)
        if p_parent != q_parent:
            for i in range(len(self.data)):
                if self.data[i] == p_parent:
                    self.data[i] = q_parent
            self.union_count -= 1
