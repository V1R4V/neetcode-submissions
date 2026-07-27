class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        maxarea = 0
        visited = set()
        
        def dfs(i,j) -> int:
            if i>=len(grid) or i<0 or j>=len(grid[0]) or j<0:
                return 0
            if grid[i][j]==0 or (i,j) in visited:
                return 0
            visited.add((i,j))
            below = dfs(i-1,j)
            above = dfs(i+1,j)
            left = dfs(i,j-1)
            right = dfs(i,j+1)

            return below+above+left+right+1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and (i,j) not in visited:
                    maxarea = max(maxarea,dfs(i,j))
        return maxarea





        