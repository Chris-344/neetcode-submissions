class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW,COL=len(grid),len(grid[0])
        que=collections.deque()
        visited=set()

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j]==2:
                    visited.add((i,j))
                    que.append((i,j))
        
        def addFrt(a,b):
            if (a==ROW or a<0 or b==COL or b<0 
            or grid[a][b]!=1 or (a,b) in visited):
                return
            que.append((a,b))
            visited.add((a,b))
            grid[a][b]=2
        
        curr=-1
        while que:
            for _ in range(len(que)):
                r,c=que.popleft()
                visited.add((r,c))
                addFrt(r+1,c)
                addFrt(r-1,c)
                addFrt(r,c+1)
                addFrt(r,c-1)
            curr+=1

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j]==1:
                    return -1
        return max(0,curr)
