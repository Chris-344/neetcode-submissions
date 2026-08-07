class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW,COL=len(board),len(board[0])
        def capture(r,c):
            if (r==ROW or c==COL or 
            r<0 or c<0 or board[r][c]!="O"):
                return
            board[r][c]="T"
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)
        
        for i in range(ROW):
            for j in range(COL):
                if (board[i][j]=="O" and (i in [0,ROW-1] or j in [0,COL-1])):
                    capture(i,j)
                
        for i in range(ROW):
            for j in range(COL):
                if board[i][j]=="O":
                    board[i][j]="X"
        
        for i in range(ROW):
            for j in range(COL):
                if board[i][j]=="T":
                    board[i][j]="O"
        