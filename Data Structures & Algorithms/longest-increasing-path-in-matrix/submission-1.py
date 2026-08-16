class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW,COL=len(matrix),len(matrix[0])
        dp={}

        def dfs(i,j,prevVal):
            if i>=ROW or j>=COL or i<0 or j<0 or matrix[i][j]<=prevVal:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            
            curr=matrix[i][j]

            dp[(i,j)]=1 + max(
                dfs(i+1,j,curr),
                dfs(i,j+1,curr),
                dfs(i-1,j,curr),
                dfs(i,j-1,curr)
            )
            return dp[(i,j)]
        res=0
        for i in range(ROW):
            for j in range(COL):
                res=max(res,dfs(i,j,-1))
        return res