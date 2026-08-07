class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW,COL=len(heights),len(heights[0])

        atl,pac=set(),set()

        def dfs(r,c,visited,prevHeight):
            if (r==ROW or r<0 or c==COL or c<0 
            or (r,c) in visited or prevHeight>heights[r][c]):
                return
            visited.add((r,c))
            dfs(r+1,c,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])
        
        for r in range(len(heights)):
            dfs(r,0,atl,0)
            dfs(r,COL-1,pac,0)
        for c in range(len(heights[0])):
            dfs(0,c,atl,0)
            dfs(ROW-1,c,pac,0)

        res=atl & pac
        return list(res)