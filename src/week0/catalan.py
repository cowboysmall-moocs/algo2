import sys


CATALAN    = {0: 1, 1: 1}

def catalan(n):
    if n in CATALAN:
        return CATALAN[n]
    else:
        c = 0

        for i in xrange(1, n + 1):
            c += catalan(i - 1) * catalan(n - i)

        CATALAN[n] = c
        return c


def main(argv):
    print catalan(int(argv[0]))


if __name__ == "__main__":
    main(sys.argv[1:])
