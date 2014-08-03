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





if __name__ == "__main__":
    main(sys.argv[1:])
