import collections
from typing import List

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:
    # TODO - you fill in here.
    path = []
    def search_maze_helper(curr):
        if not ((0 <= curr.x < len(maze)) and (0 <= curr.y < len(maze[curr.x])) and maze[curr.x][curr.y] == WHITE):
            return False

        path.append(curr)
        maze[curr.x][curr.y] = BLACK
        if curr == e:
            return True

        if any(map(search_maze_helper, \
            map(Coordinate, (curr.x+1, curr.x-1, curr.x, curr.x), \
                (curr.y, curr.y, curr.y+1, curr.y-1)))):
            return True

        del path[-1]
        return False

    search_maze_helper(s)
    return path
