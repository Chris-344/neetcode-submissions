class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW,COL=len(board),len(board[0])
        visited=set()
        
        def dfs(r,c,ptr):
            if ptr==len(word):
                return True
            if (r<0 or c<0 or r==ROW or c==COL or board[r][c]!=word[ptr] or (r,c) in visited):
                return
                
            visited.add((r,c))

            res=(
                dfs(r+1,c,ptr+1) or 
                dfs(r-1,c,ptr+1) or 
                dfs(r,c+1,ptr+1) or 
                dfs(r,c-1,ptr+1))

            visited.remove((r,c))

            return res
        for i in range(ROW):
            for j in range(COL):
                if dfs(i,j,0):
                    return True
        return False