from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        row, col = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        def isRotten(i, j):
            nonlocal fresh

            if (
                i >= row
                or j >= col
                or i < 0
                or j < 0
                or grid[i][j] == 0
                or grid[i][j] == 2
            ):
                return

            if (i, j) in visited:
                return

            visited.add((i, j))
            grid[i][j] = 2
            q.append([i, j])
            fresh -= 1

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append([i, j])
                    visited.add((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0

        mins = -1

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                isRotten(r - 1, c)
                isRotten(r + 1, c)
                isRotten(r, c - 1)
                isRotten(r, c + 1)

            mins += 1

        return mins if fresh == 0 else -1