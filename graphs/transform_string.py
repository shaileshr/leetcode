from typing import Set
import collections
import string

def transform_string(D: Set[str], s: str, t: str) -> int:
    # TODO - you fill in here.
    StringDistance = collections.namedtuple('StringDistance', ('string', 'distance'))
    q = collections.deque([])
    q.append(StringDistance(s, 0))
    D.remove(s)
    result = []
    while q:
        node_distance = q.popleft()
        node = node_distance.string
        if node == t:
            return node_distance.distance

        for i in range(len(node)):
            for c in string.ascii_lowercase:
                if node[:i]+c+node[i+1:] in D:
                    q.append(StringDistance(node[:i]+c+node[i+1:], node_distance.distance + 1))
                    D.remove(node[:i]+c+node[i+1:])
    return -1
