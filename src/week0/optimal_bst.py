import sys


def compute_subtree_cost(A, i, j):
    return A[i][j] if i < len(A) and j < len(A) else 0


def minimum_subtree_cost(A, i, j):
    return min( [ compute_subtree_cost(A, i, r - 1) + compute_subtree_cost(A, r + 1, j) for r in xrange(i, j + 1) ] )


def optimal_bst(weights):
    n = len(weights)

    A = [[0 for _ in xrange(n)] for _ in xrange(n)]
    S = [[0 for _ in xrange(n)] for _ in xrange(n)]

    for i in xrange(n):
        A[i][i] = weights[i]
        S[i][i] = weights[i]
        for j in xrange(i + 1, n):
            S[i][j] = S[i][j - 1] + weights[j]

    for s in xrange(1, n):
        for i in xrange(n - s):
            A[i][i + s] = S[i][i + s] + minimum_subtree_cost(A, i, i + s)

    return A[0][n - 1]


def main(argv):
    bst1 = [0.05, 0.4, 0.08, 0.04, 0.1, 0.1, 0.23]
    bst2 = [0.2, 0.05, 0.17, 0.1, 0.2, 0.03, 0.25]
    bst3 = [4, 2, 1, 3, 5, 2, 1]
    bst4 = [4, 1, 1, 2, 8, 16]

    print
    print '  Optimal BSTs'
    print
    print '  frequencies: %s' % (bst1)
    print '  search time: %s' % (optimal_bst(bst1))
    print
    print '  frequencies: %s' % (bst2)
    print '  search time: %s' % (optimal_bst(bst2))
    print
    print '  frequencies: %s' % (bst3)
    print '  search time: %s' % (optimal_bst(bst3))
    print
    print '  frequencies: %s' % (bst4)
    print '  search time: %s' % (optimal_bst(bst4))
    print


if __name__ == "__main__":
    main(sys.argv[1:])
