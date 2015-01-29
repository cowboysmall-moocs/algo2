import sys


CATALAN    = {0: 1, 1: 1}

def catalan(n):
    if n not in CATALAN:
        c = 0

        for i in xrange(1, n + 1):
            c += catalan(i - 1) * catalan(n - i)

        CATALAN[n] = c

    return CATALAN[n]


def main(argv):
    sys.setrecursionlimit(1048576)

    print catalan(int(argv[0]))


if __name__ == "__main__":
    main(sys.argv[1:])
