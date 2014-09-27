import sys
import math
import random

from collections import defaultdict
from itertools import chain


def construct(file_path):
    clauses = {} 
    values  = defaultdict(list)

    with open(file_path) as file:
        file.readline()

        for line in file:
            item = line.split()
            item_1 = int(item[0])
            item_2 = int(item[1])
            values[item_1].append((item_1, item_2))
            values[item_2].append((item_1, item_2))
            clauses[(item_1, item_2)] = [item_1, item_2]

    return clauses, values


def preprocess(clauses, values):
    candidates = redundant(values.keys())

    while candidates:
        for value in candidates:
            for clause in values[value]:
                values[clause[0]].remove(clause)
                values[clause[1]].remove(clause)
                del clauses[clause]

        candidates = redundant(chain(*clauses.values()))

    return clauses.keys()


def redundant(values):
    reduced = set(values)
    return set([value for value in reduced if -value not in reduced])


def satisfiable(clauses):
    n = len(clauses)

    if n == 0: 
        return True

    for _ in xrange(int(math.log(n, 2))):
        assignment = intitial_assignment(clauses)
        for _ in xrange(2 * pow(n, 2)):
            unsatisfied_clauses = unsatisfied(clauses, assignment)
            if not unsatisfied_clauses:
                return True
            else:
                flip_index = abs(random.choice(random.choice(unsatisfied_clauses)))
                assignment[flip_index] = not assignment[flip_index]

    return False


def intitial_assignment(clauses):
    assignment = {}

    for clause in clauses:
        assignment[abs(clause[0])] = random.choice([True, False])
        assignment[abs(clause[1])] = random.choice([True, False])

    return assignment


def unsatisfied(clauses, assignment):
    unsatisfied_clauses = []

    for clause in clauses:
        if unsatisfied_value(clause[0], assignment) and unsatisfied_value(clause[1], assignment):
            unsatisfied_clauses.append(clause)

    return unsatisfied_clauses


def unsatisfied_value(value, assignment):
    return (value < 0 and assignment[-value]) or (value > 0 and not assignment[value])


def main(argv):
    clauses, values = construct(argv[0])

    if satisfiable(preprocess(clauses, values)):
        print
        print 'Satisfiable'
        print
    else:
        print
        print 'Unsatisfiable'
        print


if __name__ == "__main__":
    main(sys.argv[1:])
