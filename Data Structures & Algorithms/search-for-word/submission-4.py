class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW,COL=len(board),len(board[0])
        path=set()

        def dfs(i,r,c):
            if i==len(word):
                return True
            if r<0 or c<0 or r>=ROW or c>=COL or board[r][c]!=word[i] or (r,c) in path:
                return

            path.add((r,c))

            res= (
            dfs(i+1,r+1,c) or 
            dfs(i+1,r-1,c) or 
            dfs(i+1,r,c+1) or
            dfs(i+1,r,c-1)
            )

            path.remove((r,c))
            return res
        for r in range(ROW):
            for c in range(COL):
                if dfs(0,r,c):
                    return True
        return False