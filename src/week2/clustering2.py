import sys

from union_find import UnionFind


def construct(file_path):
    vertices = []

    with open(file_path) as file:
        totals = file.readline().split()
        vtotal = int(totals[0])

        counter = 1
        for line in file:
            string = line.strip()
            number = int(''.join(string.split()), 2)

            vertices.append((number, counter))
            counter += 1

    return (vtotal, vertices)


def hamming_distance(x, y):
    count, xor = 0, x ^ y
    while xor:
        count += 1
        xor &= xor - 1
    return count


def main(argv):
    vtotal, vertices = construct(argv[0])

    vertices = sorted(vertices)
    uf       = UnionFind(vtotal)

    for i in range(vtotal):
        for j in range(i + 1, vtotal):
            if not uf.connected(vertices[i][1], vertices[j][1]):
                if hamming_distance(vertices[i][0], vertices[j][0]) <= 2:
                    uf.union(vertices[i][1], vertices[j][1])

    print
    print '%s clusters' % (uf.count())
    print


if __name__ == "__main__":
    main(sys.argv[1:])
