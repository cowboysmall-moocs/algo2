import sys
import heapq
import random

from collections import defaultdict


heap = []


def construct_graph(file_path):
    vertices = defaultdict(list)

    with open(file_path) as file:
        totals = file.readline().split()
        vtotal = totals[0]
        etotal = totals[1]

        for line in file:
            elements = line.split()
            one      = int(elements[0])
            other    = int(elements[1])
            weight   = int(elements[2])

            vertices[one].append((weight, one, other))
            vertices[other].append((weight, other, one))

    return (vtotal, etotal, vertices)


def handle_node(G, X, s):
    X.add(s)
    for edge in G[s]:
        heapq.heappush(heap, edge)


def main(argv):
    vtotal, etotal, G = construct_graph(argv[0])

    V = set(G.keys())
    X = set([])
    T = set([])

    s = random.choice(G.keys())
    handle_node(G, X, s)

    while X != V:
        edge = heapq.heappop(heap)
        if edge[2] not in X:
            T.add(edge)
            handle_node(G, X, edge[2])

    cost = 0
    for edge in T:
        cost += edge[0]

    print 
    print 'Graph'
    print 'Vertex Count: ', vtotal
    print '  Edge Count: ', etotal
    print
    print 'MST'
    print 'Overall Cost: ', cost
    print '  Edge Count: ', len(T)
    print


if __name__ == "__main__":
    main(sys.argv[1:])
