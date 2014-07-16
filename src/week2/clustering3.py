import sys
import itertools

from collections import defaultdict
from union_find import UnionFind


def construct(file_path):
    vertices = {}

    with open(file_path) as file:
        file.readline()

        count = 0
        for line in file:
            number = int(''.join(line.strip().split()), 2)
            vertices[number] = count
            count += 1

    return vertices



def generate_distances(bit_count, distance):
    result = []
    for bits in itertools.combinations(range(bit_count), distance):
        zeros = ['0'] * bit_count
        for bit in bits:
            zeros[bit] = '1'
        result.append(int(''.join(zeros), 2))
    return result



def main(argv):
    vertices  = construct(argv[0])
    distances = generate_distances(24, 2) + generate_distances(24, 1)

    uf = UnionFind(len(vertices))

    for vertex in vertices:
        for distance in distances:
            candidate = vertex ^ distance
            if candidate in vertices:
                if not uf.connected(vertices[vertex], vertices[candidate]):
                    uf.union(vertices[vertex], vertices[candidate])

    print
    print '%s clusters' % (uf.count())
    print


if __name__ == "__main__":
    main(sys.argv[1:])
