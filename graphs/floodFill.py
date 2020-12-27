# 733. Flood Fill
# https://leetcode.com/problems/flood-fill/
# Easy
#
# 1642
#
# 223
#
# Add to List
#
# Share
# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
#
# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
#
# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.
#
# At the end, return the modified image.
#
# Example 1:
# Input:
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation:
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
# by a path of the same color as the starting pixel are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected
# to the starting pixel.
# Note:
#
# The length of image and image[0] will be in the range [1, 50].
# The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
# The value of each color in image[i][j] and newColor will be an integer in [0, 65535].

from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return image

        self.color = image[sr][sc]
        self.m = len(image)
        self.n = len(image[0])

        def check_valid(r, c):


            if 0<= r < self.m and 0 <= c < self.n and image[r][c] == self.color:
                return True

            return False


        def bfs(sr, sc, newColor):
            q = collections.deque()
            seen = set()
            q.append((sr, sc))
            seen.add((sr, sc))
            image[sr][sc] = newColor

            while q:
                r, c = q.popleft()
                for new_r, new_c in (r+1, c), (r -1, c), (r, c+1), (r, c-1):

                    if (new_r, new_c) not in seen and check_valid(new_r, new_c):
                        q.append((new_r, new_c))
                        seen.add((new_r, new_c))
                        image[new_r][new_c] = newColor


            return image

        def dfs(r, c, newColor):
            if image[r][c] == newColor:
                return image

            image[r][c] = newColor

            for new_r, new_c in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if check_valid(new_r, new_c):
                        dfs(new_r, new_c, newColor)

            return image


        return dfs(sr,sc,newColor)
        #return bfs(sr, sc, newColor)



