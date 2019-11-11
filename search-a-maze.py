"""
It is natural to apply graph models and algorithms to spatial problems. Consider
a black and white digitized image of a maze—white pixels represent open areas
and black spaces are walls. There are two special white pixels: one is
designated the entrance and the other is the exit. The goal in this problem is
to find a way of getting from the entrance to the exit, as illustrated in Figure
18.5 on the next page.

Given a 2D array of black and white entries representing a maze with designated
entrance and exit points, find a path from the entrance to the exit, if one
exists.

Hint: Model the maze as a graph.

NOTES:
- Since the problem did not call for a shortest path, it is better to use DFS.

"""

from collections import namedtuple


WHITE, BLACK = range(2)

Coordinate = namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze, s, e):
    """
    Time complexity: O(|V| + |E|)

    """

    def search_maze_helper(cur):
        if not (0 <= cur.x < len(maze) and 0 <= cur.y < len(maze[cur.x]) and \
            maze[cur.x][cur.y] == WHITE):
            return False
        path.append(cur)
        maze[cur.x][cur.y] = BLACK
        if cur == e:
            return True

        if any(
            map(
                search_maze_helper,
                (
                    Coordinate(cur.x - 1, cur.y),
                    Coordinate(cur.x + 1, cur.y),
                    Coordinate(cur.x, cur.y - 1),
                    Coordinate(cur.x, cur.y + 1)
                )
            )
        ):
            return True
        del path[-1]
        return False

    path = []
    if not search_maze_helper(s):
        return []
    return path
