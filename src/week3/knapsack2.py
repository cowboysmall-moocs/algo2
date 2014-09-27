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


def relevant_entries(W, n, items):
    entries = []

    relevant_entries = defaultdict(list)
    relevant_entries[n].append(W)

    for i in xrange(n - 1, 0, -1):
        no_dupes     = set(relevant_entries[i + 1] + [w - items[i - 1][0] for w in relevant_entries[i + 1]])
        non_negative = [entry for entry in no_dupes if entry >= 0]
        relevant_entries[i].extend(non_negative)

    for key, values in relevant_entries.iteritems():
        for value in values:
            entries.append((key, value))

    return entries


def knapsack(entries, items):
    A = defaultdict(int)

    for entry in entries:
        left_entry = (entry[0] - 1, entry[1])
        if items[entry[0] - 1][0] <= entry[1]:
            current_weight = items[entry[0] - 1][0]
            current_value  = items[entry[0] - 1][1]
            previous_entry = (entry[0] - 1, entry[1] - current_weight)
            A[ entry ] = max( A[ left_entry ], A[ previous_entry ] + current_value)
        else:
            A[ entry ] = A[ left_entry ]

    return A


def main(argv):
    W, n, items = construct(argv[0])
    entries     = relevant_entries(W, n, items)
    A           = knapsack(entries, items)

    print
    print '                Dimensions of problem (n x W): ', (W * n)
    print '                    Count of relevant entries: ', len(entries)
    print 'Percentage of relevant entries to all entries: ', (float(len(entries)) / (W * n)) * 100
    print '            Count of calculated entries (|A|): ', len(A)
    print '                                    A[(n, W)]: ', A[(n, W)]
    print


if __name__ == "__main__":
    main(sys.argv[1:])
