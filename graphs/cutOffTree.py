from typing import List

from collections import namedtuple
from collections import deque
def cutOffTree(forest: List[List[int]]) -> int:

    def bfs(sr, sc, tr, tc):
        m, n = len(forest), len(forest[0])

        seen = set()
        q = deque()
        q.append((sr, sc, 0))
        seen.add((sr, sc))
        while q:
            r, c, d = q.popleft()
            if r == tr and c == tc:
                return d


            for new_r, new_c in ((r+1, c), (r - 1, c), (r, c+1), (r, c-1)):
                if (new_r, new_c) not in seen and 0 <= new_r < m and 0 <= new_c < n and forest[new_r][new_c]:
                    q.append((new_r, new_c, d+1))
                    forest[new_r][new_c] = 1
                    seen.add((new_r, new_c))

        return -1

    if not forest:
        return -1

    trees = sorted([(v, r, c) for r,row in enumerate(forest) for c,v in enumerate(row) if v > 1])
    sr, sc = 0, 0

    totalCost = 0
    for _, tr, tc in trees:
        cost = bfs(sr, sc, tr, tc)
        if cost == -1:
            return -1
        totalCost += cost
        sr, sc = tr, tc





    return totalCost

def main():
    forest = [[2,3,4],[0,0,5],[8,7,6]]
    print(cutOffTree(forest))

main()
