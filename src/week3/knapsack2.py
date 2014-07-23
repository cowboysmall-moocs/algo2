import sys

from collections import defaultdict


def construct(file_path):
    items = []

    with open(file_path) as file:
        first = file.readline().split()
        W = int(first[0])
        n = int(first[1])

        for line in file:
            item = line.split()
            items.append((int(item[1]), int(item[0])))

    return (W, n, sorted(items))


def main(argv):
    W, n, items = construct(argv[0])


    ix = defaultdict(list)
    ix[n].append(W)
    for i in range(n - 1, 0, -1):
        temp  = set(ix[i + 1] + [w - items[i - 1][0] for w in ix[i + 1]])
        ix[i].extend([t for t in temp if t >= 0])


    entries = []
    for key, values in ix.iteritems():
        for value in values:
            entries.append((key, value))


    A = defaultdict(int)
    for entry in entries:
        if items[entry[0] - 1][0] <= entry[1]:
            A[entry] = max( A[ (entry[0] - 1, entry[1]) ], A[ (entry[0] - 1, entry[1] - items[entry[0] - 1][0]) ] + items[entry[0] - 1][1])
        else:
            A[entry] = A[ (entry[0] - 1, entry[1]) ]



    print
    print 'W x N     = ', (W * n)
    print '|entries| = ', len(entries)
    print '%         = ', (float(len(entries)) * 100) / (W * n)  
    print '|A|       = ', len(A)
    print 'Value     = ', A[(n, W)]
    print


if __name__ == "__main__":
    main(sys.argv[1:])
