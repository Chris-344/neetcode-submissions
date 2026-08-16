class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=defaultdict(list)
        
        for st,at,tt in times:
            adj[st].append((at,tt))

        minH=[]
        minH.append((0,k))
        visited=set()
        time=0
        while minH:
            w1,n1=heapq.heappop(minH)
            if n1 in visited:
                continue
            visited.add(n1)
            time=w1
            for a,b in adj[n1]:
                heapq.heappush(minH,(time+b,a))

        return time if len(visited)==n else -1