import sys
import math
import random

from collections import defaultdict
from itertools import chain


def construct(file_path):
    clauses = []

    with open(file_path) as file:
        file.readline()

        for line in file:
            item = line.split()
            clauses.append((int(item[0]), int(item[1])))

    return clauses


def satisfiable(clauses):
    n = len(clauses)

    for i in xrange(int(math.log(n, 2))):

        assignment = [random.choice([True, False]) for _ in range(n)]
        for j in xrange(2 * pow(n, 2)):
            unsatisfied_clauses = unsatisfied(clauses, assignment)
            if not unsatisfied_clauses:
                return True
            else:
                flip_index = abs(random.choice(unsatisfied_clauses)[random.randint(0, 1)]) - 1
                assignment[flip_index] = not assignment[flip_index]

    return False


def unsatisfied(clauses, assignment):
    unsatisfied_clauses = []
    for clause in clauses:
        clause_1 = (clause[0] < 0 and assignment[abs(clause[0]) - 1]) or (clause[0] > 0 and not assignment[abs(clause[0]) - 1])
        clause_2 = (clause[1] < 0 and assignment[abs(clause[1]) - 1]) or (clause[1] > 0 and not assignment[abs(clause[1]) - 1])
        if clause_1 and clause_2:
            unsatisfied_clauses.append(clause)
    return unsatisfied_clauses


def preprocess(clauses):
    values_dict  = defaultdict(set)

    for clause in clauses:
        values_dict[clause[0]].add(clause)
        values_dict[clause[1]].add(clause)

    reduced = set()
    # keys = values_dict.keys()
    # for key in keys:
    #     if -key not in values_dict:
    #         for clause in values_dict[key]:
    #             if clause[0] == key:
    #                 for value in values_dict[clause[1]]:
    #                     if value[0] != key or values[1] != key:
                            


    return list(reduced)


def main(argv):
    clauses = construct(argv[0])

    if satisfiable(clauses):
        print
        print 'Satisfiable'
        print
    else:
        print
        print 'Unsatisfiable'
        print


if __name__ == "__main__":
    main(sys.argv[1:])
