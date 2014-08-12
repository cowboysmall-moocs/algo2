import sys



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



def knapsack(W, n, items):
    A = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for x in range(W + 1):
            if items[i - 1][0] <= x:
                A[i][x] = max(A[i - 1][x], A[i - 1][x - items[i - 1][0]] + items[i - 1][1])
            else:
                A[i][x] = A[i - 1][x]

    return A



def main(argv):
    W, n, items = construct(argv[0])
    A           = knapsack(W, n, items)

    print
    print 'Value = ', A[n][W]
    print



if __name__ == "__main__":
    main(sys.argv[1:])
