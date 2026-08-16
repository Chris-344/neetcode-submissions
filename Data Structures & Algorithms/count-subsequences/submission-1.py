class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ROW, COL = len(s), len(t)
        grid = [[0] * (COL+1) for _ in range(ROW+1)]

        for i in range(ROW+1):
            grid[i][COL] = 1
            
        for i in range(ROW-1, -1, -1):
            for j in range(COL-1, -1, -1):
                if s[i] == t[j]:
                    grid[i][j] = grid[i+1][j+1] + grid[i+1][j]
                else:
                    grid[i][j] = grid[i+1][j]

        return grid[0][0]