import sys

from collections import defaultdict



stack   = []
index   = {}
lowlink = {}


def construct(file_path):
    graph = defaultdict(list)

    with open(file_path) as file:
        file.readline()

        for line in file:
            item = line.split()
            graph[-int(item[0])].append(int(item[1]))
            graph[-int(item[1])].append(int(item[0]))

    return graph



def scc(v, graph, components, i):
    index[v]   = i
    lowlink[v] = i

    stack.append(v)

    for w in graph[v]:
        if w not in index:
            scc(w, graph, components, i + 1)
            lowlink[v] = min(lowlink[v], lowlink[w])
        elif w in stack:
            lowlink[v] = min(lowlink[v], index[w])

    if lowlink[v] == index[v]:
        while v not in components[v]:
            components[v].append(stack.pop())



def satisfiable(graph):
    components = defaultdict(list)

    for v in graph.keys():
        if v not in index:
            scc(v, graph, components, 0)

    for root in components:
        for v in components[root]:
            if -v in components[root]:
                return False

    return True



def main(argv):
    graph = construct(argv[0])

    if satisfiable(graph):
        print
        print 'Satisfiable'
        print
    else:
        print
        print 'Unsatisfiable'
        print



if __name__ == "__main__":
    main(sys.argv[1:])
