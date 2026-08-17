class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N=len(points)
        adj={i:[] for i in range(N)}
        for i in range(N):
            for j in range(i+1,N):
                dist=abs(points[i][1]-points[j][1]) + abs(points[i][0]-points[j][0])
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        
        res=0
        visited=set()
        minH=[[0,0]]
        while len(visited)<N:
            cost,node=heapq.heappop(minH)
            if node in visited:
                continue
            res+=cost
            visited.add(node)
            for c2,n2 in adj[node]:
                if n2 not in visited:
                    heapq.heappush(minH,[c2,n2])

        return res