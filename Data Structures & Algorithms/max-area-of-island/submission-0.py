class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.res=0
        rows, cols = len(grid), len(grid[0])
        visited = [[0] * cols for _ in range(rows)]

        def bfs(matrix,row,col):
            curr=0
            ROW,COL=len(matrix),len(matrix[0])
            q=collections.deque()
            visited[row][col]=1
            q.append((row,col))

            while q:
                curr+=1
                r,c=q.popleft()
                if r+1<ROW and not visited[r+1][c] and matrix[r+1][c]:
                    visited[r+1][c]=1
                    q.append((r+1,c))
                if r-1>=0 and not visited[r-1][c] and matrix[r-1][c]:
                    visited[r-1][c]=1
                    q.append((r-1,c))
                if c+1<COL and not visited[r][c+1] and matrix[r][c+1]:
                    visited[r][c+1]=1
                    q.append((r,c+1))
                if c-1>=0 and not visited[r][c-1] and matrix[r][c-1]:
                    visited[r][c-1]=1
                    q.append((r,c-1))
            self.res=max(self.res,curr)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] and not visited[i][j]:
                    bfs(grid,i,j)

        return self.res