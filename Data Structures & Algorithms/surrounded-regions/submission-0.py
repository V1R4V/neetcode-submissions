class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row,col = len(board),len(board[0])
        def capture(r,c):
            if (r<0 or c<0 or r==row or c==col or board[r][c]!="O"):
                return
            board[r][c]="T"
            capture(r-1,c)
            capture(r+1,c)
            capture(r,c+1)
            capture(r,c-1)
        #check for areas of the grid where the marker cannot be changed from O to X
        for r in range(row):
            for c in range(col):
                if (board[r][c]=="O" and (r == 0 or c==0 or r==row-1 or c==col-1)):
                    capture(r,c)

        for r in range(row):
            for c in range(col):
                if (board[r][c]=="O"):
                    board[r][c]="X"
                    
        for r in range(row):
            for c in range(col):
                if board[r][c]=="T":
                    board[r][c] = "O"