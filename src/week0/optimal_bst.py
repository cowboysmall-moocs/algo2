import sys


def optimal_bst(weights):
    n = len(weights)
    A = [[0 for _ in xrange(n)] for _ in xrange(n + 1)]
    S = [[0 for _ in xrange(n)] for _ in xrange(n + 1)]


    for i in xrange(n):
        A[i][i] = weights[i]
        S[i][i] = weights[i]
        for j in xrange(i + 1, n):
            S[i][j] = S[i][j - 1] + weights[j]


    for s in xrange(1, n):
        for i in xrange(n - s):
            A[i][i + s] = S[i][i + s] + min( [ A[i][r - 1] + A[r + 1][i + s] for r in xrange(i, i + s + 1) ] )


    return A[0][n - 1]



def main(argv):
    bst1 = [0.05, 0.4, 0.08, 0.04, 0.1, 0.1, 0.23]
    bst2 = [0.2, 0.05, 0.17, 0.1, 0.2, 0.03, 0.25]
    bst3 = [4, 2, 1, 3, 5, 2, 1]

    print
    print '  Optimal BSTs'
    print
    print '                  frequencies: %s' % (bst1)
    print '  minimum average search time: %s' % (optimal_bst(bst1))
    print
    print '                  frequencies: %s' % (bst2)
    print '  minimum average search time: %s' % (optimal_bst(bst2))
    print
    print '                  frequencies: %s' % (bst3)
    print '  minimum average search time: %s' % (optimal_bst(bst3))
    print


if __name__ == "__main__":
    main(sys.argv[1:])
