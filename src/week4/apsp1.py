import sys


def construct(file_path):
    edges    = {}

    with open(file_path) as file:
        first = file.readline().split()
        v = int(first[0])
        e = int(first[1])

        for line in file:
            item = line.split()
            edges[(int(item[0]), int(item[1]))] = int(item[2])

    return (v, edges)


def floyd_warshall(v, edges):
    A = [[[0 for _ in xrange(v + 1)] for _ in xrange(v)] for _ in xrange(v)]

    for i in xrange(v):
        for j in xrange(v):
            if i == j:
                A[i][j][0] = 0
            elif (i + 1, j + 1) in edges:
                A[i][j][0] = edges[(i + 1, j + 1)]
            else:
                A[i][j][0] = sys.maxint

    for k in xrange(v):
        for j in xrange(v):
            for i in xrange(v):
                A[i][j][k + 1] = min(A[i][j][k], A[i][k][k] + A[k][j][k])

    for i in xrange(v):
        if A[i][i][v - 1] < 0:
            return None
            
    return A


def main(argv):
    v, e = construct(argv[0])
    A    = floyd_warshall(v, e)

    if A == None:
        print
        print 'Negative Weight Cycle Detected!'
        print
    else:
        shortest = []
        for i in xrange(v):
            for j in xrange(v):
                if i != j:
                    shortest.append((A[i][j][v], (i + 1, j + 1)))
        d, p = min(shortest)
        print
        print 'Shortest Path [%s, %s] = %s' % (p[0], p[1], d)
        print


if __name__ == "__main__":
    main(sys.argv[1:])
