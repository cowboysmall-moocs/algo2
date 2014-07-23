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


    relevant_entries = defaultdict(list)
    relevant_entries[n].append(W)
    for i in range(n - 1, 0, -1):
        no_dupes     = set(relevant_entries[i + 1] + [w - items[i - 1][0] for w in relevant_entries[i + 1]])
        non_negative = [entry for entry in no_dupes if entry >= 0]
        relevant_entries[i].extend(non_negative)


    relevant_entries_list = []
    for key, values in relevant_entries.iteritems():
        for value in values:
            relevant_entries_list.append((key, value))


    A = defaultdict(int)
    for entry in relevant_entries_list:
        left_entry = (entry[0] - 1, entry[1])
        if items[entry[0] - 1][0] <= entry[1]:
            current_weight = items[entry[0] - 1][0]
            current_value  = items[entry[0] - 1][1]
            previous_entry = (entry[0] - 1, entry[1] - current_weight)
            A[ entry ] = max( A[ left_entry ], A[ previous_entry ] + current_value)
        else:
            A[ entry ] = A[ left_entry ]


    print
    print '                Dimensions of problem (n x W): ', (W * n)
    print '                    Count of relevant entries: ', len(relevant_entries_list)
    print 'Percentage of relevant entries to all entries: ', (float(len(relevant_entries_list)) * 100) / (W * n)  
    print '            Count of calculated entries (|A|): ', len(A)
    print '                                    A[(n, W)]: ', A[(n, W)]
    print


if __name__ == "__main__":
    main(sys.argv[1:])
