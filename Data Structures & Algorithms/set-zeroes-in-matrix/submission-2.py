class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROW,COL=len(matrix),len(matrix[0])

        def dfs(r,c):
            for i in range(COL):
                if matrix[r][i]!=0:
                    matrix[r][i]="t"

            for i in range(ROW):
                if matrix[i][c]!=0:
                    matrix[i][c]="t"

        
        for i in range(ROW):
            for j in range(COL):
                if matrix[i][j]==0:
                    dfs(i,j)

        for i in range(ROW):
            for j in range(COL):
                if matrix[i][j]=="t":
                    matrix[i][j]=0