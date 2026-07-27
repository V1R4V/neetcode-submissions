class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        islands = 0
        visited = set()

        def dfs(i,j):
            if i>=len(grid) or i<0 or j>=len(grid[0]) or j<0:
                return 
            
            if (i,j) in visited or grid[i][j]=="0":
                return 

            visited.add((i,j))
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and (i,j) not in visited:
                    dfs(i,j)
                    islands+=1
                    
        return islands
