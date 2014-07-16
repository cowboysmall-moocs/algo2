import sys

from union_find import UnionFind


def construct_edges(file_path):
    edges = []

    with open(file_path) as file:
        vtotal = int(file.readline())

        for line in file:
            elements = line.split()
            one      = int(elements[0])
            other    = int(elements[1])
            weight   = int(elements[2])

            edges.append((weight, one, other))

    return (vtotal, edges)


def main(argv):
    vtotal, edges = construct_edges(argv[0])

    edges = sorted(edges)
    uf    = UnionFind(vtotal)
    k     = int(argv[1])
    T     = set([])

    max_spacing = 0
    while uf.count() >= k:
        edge = edges.pop(0)
        if not uf.connected(edge[1], edge[2]):
            uf.union(edge[1], edge[2])
            max_spacing = edge[0]

    print
    print 'For %s clustering: max spacing = %s' % (k, max_spacing)
    print



if __name__ == "__main__":
    main(sys.argv[1:])
