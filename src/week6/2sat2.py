import sys
import math
import random

from collections import defaultdict



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

    for _ in xrange(int(math.log(n, 2))):
        assignment = [random.choice([True, False]) for _ in range(n)]
        for _ in xrange(2 * pow(n, 2)):
            unsatisfied_clauses = unsatisfied(clauses, assignment)
            if not unsatisfied_clauses:
                return True
            else:
                flip_index = abs(random.choice(random.choice(unsatisfied_clauses))) - 1
                assignment[flip_index] = not assignment[flip_index]

    return False



def unsatisfied(clauses, assignment):
    unsatisfied_clauses = []

    for clause in clauses:
        if unsatisfied_value(clause[0], assignment) and unsatisfied_value(clause[1], assignment):
            unsatisfied_clauses.append(clause)

    return unsatisfied_clauses



def unsatisfied_value(value, assignment):
    return (value < 0 and assignment[-value - 1]) or (value > 0 and not assignment[value - 1])



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
