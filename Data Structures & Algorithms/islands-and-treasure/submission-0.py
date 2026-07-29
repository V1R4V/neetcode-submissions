class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row,col = len(grid),len(grid[0])
        visited = set()
        q = deque()

        def addCell(r,c):
            if r<0 or c<0 or r>=row or c>=col or (r,c) in visited or grid[r][c]==-1:
                return
            visited.add((r,c))
            q.append([r,c])

        #this runs first because this finds the first treasure 
        for r in range(row):
            for c in range(col):
                if grid[r][c]==0:
                    q.append([r,c])
                    visited.add((r,c))
        #once q is made we traverse the q (only items with treasure)
        dist=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]= dist
                addCell(r + 1, c) # all added to q and will be marked 1 in the next iteration
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist+=1






        


        