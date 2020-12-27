import collections
from typing import List

class GraphVertex:
    def __init__(self, label) -> None:
        self.label = label
        self.d = -1
        self.edges: List[GraphVertex] = []

    def __str__(self):
        return str(self.label)


def is_any_placement_feasible(graph: List[GraphVertex]) -> bool:
    # TODO - you fill in here.
    def bfs(s):
        s.d = 0
        q = collections.deque([s])
        while q:
            print('q[0] with d')
            print(str(q[0]) + ' ' + str(q[0].d))
            for t in q[0].edges:
                print('t with d')
                print(str(t) + ' ' + str(t.d))
                if t.d == -1:
                    t.d = q[0].d + 1
                    q.append(t)
                elif t.d == q[0].d:
                    return False
            del q[0]
        return True

    return all(bfs(v) for v in graph if v.d == -1)

def is_any_placement_feasible_wrapper(k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex(i) for i in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])
    return graph

def main():
    graph = is_any_placement_feasible_wrapper(3, [[0, 1], [1,0], [1, 2], [2,1], [2, 0], [0, 2]])

    print(is_any_placement_feasible(graph))

main()
