# https://leetcode.com/problems/max-area-of-island/

#
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
#
# Example 1:
#
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
# Example 2:
#
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# Note: The length of each dimension in the given grid does not exceed 50.
from typing import List
def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


###########DFS Recursive
#         def maxAreaOfIsland_helper_dfs(x,y):
#             if not ((0 <= x < len(grid)) and (0 <= y < len(grid[x])) and \
#                    grid[x][y]):
#                 return 0

#             grid[x][y] = 0


#             return 1 + \
#                 maxAreaOfIsland_helper_dfs(x+1, y) + \
#                 maxAreaOfIsland_helper_dfs(x-1, y) + \
#                 maxAreaOfIsland_helper_dfs(x, y+1) + \
#                 maxAreaOfIsland_helper_dfs(x, y-1)


#         areas = [maxAreaOfIsland_helper_dfs(i, j)
#                    for i in range(len(grid))
#                    for j in range(len(grid[i])) if grid[i][j]]
#         return max(areas) if areas else 0

###########DFS Iterative
            maxArea = 0
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j]:
                        stack = []
                        currentArea = 0
                        stack.append((i,j))

                        while stack:
                            (r,c) = stack.pop()
                            currentArea += 1
                            grid[r][c] = 0

                            for new_r, new_c in ((r+1, c), (r-1,c), (r, c+1), (r, c-1)):
                                if (0<= new_r< len(grid)) and (0<=new_c < len(grid[0])) and grid[new_r][new_c]:
                                    stack.append((new_r, new_c))
                                    grid[new_r][new_c] = 0
                        maxArea = max(maxArea, currentArea)

            return maxArea