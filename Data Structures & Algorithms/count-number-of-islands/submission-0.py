class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.res=0
        rows, cols = len(grid), len(grid[0])
        visited = [[0] * cols for _ in range(rows)]
        
        def bfs(r,c):
            self.res+=1
            visited[r][c]=1
            que=[]
            que.append((r,c))
            while que:
                cur_row,cur_col=que.pop(0)
                if (cur_row-1 >= 0 and grid[cur_row-1][cur_col]=="1" and not visited[cur_row-1][cur_col]):
                    visited[cur_row-1][cur_col]=1
                    que.append((cur_row-1,cur_col))

                
                if (cur_col -1>= 0 and grid[cur_row][cur_col-1]=="1" and not visited[cur_row][cur_col-1]):
                    visited[cur_row][cur_col-1]=1
                    que.append((cur_row,cur_col-1))
                
                if (cur_row +1 < len(grid) and grid[cur_row+1][cur_col]=="1" and not visited[cur_row+1][cur_col]):
                    visited[cur_row+1][cur_col]=1
                    que.append((cur_row+1,cur_col))
                
                if (cur_col +1 < len(grid[0]) and grid[cur_row][cur_col+1]=="1" and not visited[cur_row][cur_col+1]):
                    visited[cur_row][cur_col+1]=1
                    que.append((cur_row,cur_col+1))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=="0":
                    visited[row][col]=1
                    continue                    
                if grid[row][col]=="1" and not visited[row][col]:
                    bfs(row,col)

        return self.res