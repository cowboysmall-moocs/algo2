import sys

from itertools import combinations, chain


def construct(file_path):
    vertices = []

    with open(file_path) as file:
        count = int(file.readline())

        for line in file:
            item = line.split()
            vertices.append((float(item[0]), float(item[1])))

    return (count, vertices)



def main(argv):
    count, vertices = construct(argv[0])
    destinations    = list(range(1, count))
    distances       = generate_distances(vertices)

    # first = vertices[0]

    # A = [[0 for _ in range(count - 1)] for _ in range(2 ** (count - 1))]

    # for i in range(count - 1):
    #     A[i][0] = sys.maxint


    # for m in range(2, count)




if __name__ == "__main__":
    main(sys.argv[1:])
