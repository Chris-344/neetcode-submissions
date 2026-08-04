class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path=set()
        ROW,COL=len(board),len(board[0])

        def dfs(r,c,i):
            if i==len(word):
                return True

            if (r<0 or r>=ROW or c<0 or c>=COL or i>len(word)
            or board[r][c]!=word[i] or (r,c) in path):
                return 0

            
            path.add((r,c))            

            res=(dfs(r+1,c,i+1) or
            dfs(r-1,c,i+1) or
            dfs(r,c+1,i+1) or
            dfs(r,c-1,i+1)
            )
            path.remove((r,c))
            return res

        for l in range(ROW):
            for m in range(COL):
                if dfs(l,m,0):return True
        return False