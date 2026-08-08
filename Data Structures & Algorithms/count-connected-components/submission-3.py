class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:    
        adj={i:[] for i in range(n)}

        for fr,to in edges:
            adj[fr].append(to)
            adj[to].append(fr)

        if n<=1:
            return n

        visited=set()
        def dfs(curr):
            if adj[curr]==[]:
                visited.add(curr)
                return
            if curr in visited:
                return
            visited.add(curr)
            for j in adj[curr]:
                dfs(j)

        self.total=0
        while len(visited)!=n:
            for i in range(n):
                if i not in visited:
                    self.total+=1
                    dfs(i)
        return self.total
