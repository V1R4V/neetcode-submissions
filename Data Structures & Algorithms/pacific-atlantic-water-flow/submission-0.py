class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # if the neighboring cell's height is less than or equal to the current cell's height.
        #reverse search -> the problem expects that from a given cell can the water flow to both pac and atlantic so if we start from 5 which is literally the middle we can go to left 5->4->2 and 5->3->1 and we can go up and down as well. 
        pac,at= set(),set()
        row,col = len(heights),len(heights[0])


        def dfs(r,c,visit,height):
            """ because we are doing reverse so water is coming in and the question gives us the condition to neighboring cell's height is less than or equal to the current cell's height we need to have elements which are larger or equal when coming in ... if we were starting from an element lets say 5 and going out then we would have done less than equal to blocks which make sense ! however we are coming in from ocean elements to center (try to think both ways in both direction and satisfy the condition on each block)"""
            if (((r,c)in visit) or r<0 or c<0 or r>=row or c>=col or heights[r][c]<height): 
                return 
            visit.add((r,c))
            h=heights[r][c]
            dfs(r+1,c,visit,h)
            dfs(r-1,c,visit,h)
            dfs(r,c+1,visit,h)
            dfs(r,c-1,visit,h)

        #start a dfs from all atlantic ocean and pacific ocean sides (these will be row 0 and row 4)
        for c in range(col): #for each column in row 0 and len row -1 call dfs on elements
            dfs(0,c,pac,heights[0][c])
            dfs(row-1,c,at,heights[row-1][c])
        
        #start a dfs from all atlantic ocean and pacific ocean sides (these will be col 0 and col 4)
        for r in range(row): #for each row in col 0 and len col -1 call dfs on elements
            dfs(r,0,pac,heights[r][0])
            dfs(r,col-1,at,heights[r][col-1])
        ans=[]
        for r in range(row):
            for c in range(col):
                if (r,c) in pac and (r,c) in at:
                    ans.append([r,c])
        return ans

        



        
        