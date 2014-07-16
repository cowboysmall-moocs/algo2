import sys

from collections import defaultdict
from union_find import UnionFind


def construct(file_path):
    vertices = defaultdict(list)
    indices  = {}

    with open(file_path) as file:
        file.readline()

        count = 0
        for line in file:
            string = ''.join(line.strip().split())
            number = int(string, 2)

            if number not in vertices:
                vertices[number].extend(generate_hamming_list_integers(string, 2))
                vertices[number].extend(generate_hamming_list_integers(string, 1))
                indices[number] = count
                count += 1

    return (vertices, indices)



def generate_hamming_list_integers(bit_string, distance):
    return [int(string, 2) for string in generate_hamming_list(bit_string, distance)]



def generate_hamming_list(bit_string, distance):
    if distance == 0:
        return [bit_string]
    else:
        hamming_list = []
        for index in range(len(bit_string)):
            if len(bit_string[index:]) > distance - 1:
                if bit_string[index] == "0":
                    rest_of_list = generate_hamming_list(bit_string[index + 1:], distance - 1)
                    hamming_list.extend(map(lambda x: bit_string[:index] + "1" + x, rest_of_list))
                else:
                    rest_of_list = generate_hamming_list(bit_string[index + 1:], distance - 1)
                    hamming_list.extend(map(lambda x: bit_string[:index] + "0" + x, rest_of_list))                
        return hamming_list



def main(argv):
    vertices, indices = construct(argv[0])

    uf = UnionFind(len(vertices))
    for vertex, candidates in vertices.iteritems():
        for candidate in candidates:
            if candidate in indices and not uf.connected(indices[vertex], indices[candidate]):
                uf.union(indices[vertex], indices[candidate])

    print
    print '%s clusters' % (uf.count())
    print


if __name__ == "__main__":
    main(sys.argv[1:])
