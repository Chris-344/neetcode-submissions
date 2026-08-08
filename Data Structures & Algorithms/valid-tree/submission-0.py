class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        gMap={i:[] for i in range(n)}

        for e,d in edges:
            gMap[e].append(d)
            gMap[d].append(e)


        visited=set()
        def dfs(curr,prev):
            if curr in visited:
                return False
            visited.add(curr)
            for i in gMap[curr]:
                if i==prev:
                    continue
                if not dfs(i,curr):return False
            return True

        return dfs(0,-1) and len(visited)==n