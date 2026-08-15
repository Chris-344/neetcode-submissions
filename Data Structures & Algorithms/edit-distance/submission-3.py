class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        grid=[[0] * (len(word1)+1) for _ in range(len(word2)+1)]

        for i in range(len(grid)-1,-1,-1):
            grid[i][-1]=len(word2)-i
        for i in range(len(grid[0])-1,-1,-1):
            grid[-1][i]=len(word1)-i
        
        for j in range(len(word2)-1,-1,-1):
            for k in range(len(word1)-1,-1,-1):
                if word1[k]==word2[j]:
                    grid[j][k]=grid[j+1][k+1]
                else:
                    grid[j][k]=1+min(grid[j+1][k+1],grid[j+1][k],grid[j][k+1])
        return grid[0][0]
        