import sys


def construct(file_path):
    clauses = []

    with open(file_path) as file:
        file.readline()

        for line in file:
            item = line.split()
            clauses.append((int(item[0]), int(item[1])))

    return clauses



def main(argv):
    clauses = construct(argv[0])

    if satisfiable(components):
        print
        print 'Satisfiable'
        print
    else:
        print
        print 'Unsatisfiable'
        print


if __name__ == "__main__":
    main(sys.argv[1:])
