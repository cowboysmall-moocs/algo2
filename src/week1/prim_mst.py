import sys
import heapq

from collections import defaultdict



# distances = {}


# def construct_graph(file_path):
#     # edges    = {}
#     vertices = defaultdict(list)
#     with open(file_path) as file:
#         totals = file.readline().split()
#         # vtotal = totals[0]
#         # etotal = totals[1]
#         for line in file:
#             elements = line.split()
#             tail     = int(elements[0])
#             head     = int(elements[1])
#             weight   = int(elements[2])

#             vertices[tail].append((weight, head, tail))
#             vertices[head].append((weight, tail, head))


#             # edges[(tail, head)] = weight
#             # edges[(head, tail)] = weight

#     return vertices


# def main(argv):
#     vertices = construct_graph(argv[0])
#     heap     = [(0, None, 1)]
#     X        = []
#     T        = {}


#     while len(X) != len(vertices):
#         _, h, t = heapq.heappop(heap)
#         if 
            


if __name__ == "__main__":
    main(sys.argv[1:])
