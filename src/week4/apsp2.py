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
    A = [[0 for _ in xrange(v)] for _ in xrange(v)]
    B = [[0 for _ in xrange(v)] for _ in xrange(v)]


    for i in xrange(v):
        for j in xrange(v):
            if i == j:
                B[i][j] = 0
            elif (i + 1, j + 1) in edges:
                B[i][j] = edges[(i + 1, j + 1)]
            else:
                B[i][j] = sys.maxint


    for k in xrange(v):
        for j in xrange(v):
            for i in xrange(v):
                A[i][j] = min(B[i][j], B[i][k] + B[k][j])
        for j in xrange(v):
            for i in xrange(v):
                B[i][j] = A[i][j]


    for i in xrange(v):
        if A[i][i] < 0:
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
                    shortest.append((A[i][j], (i + 1, j + 1)))
        d, p = min(shortest)
        print
        print 'Shortest Path [%s, %s] = %s' % (p[0], p[1], d)
        print



if __name__ == "__main__":
    main(sys.argv[1:])
