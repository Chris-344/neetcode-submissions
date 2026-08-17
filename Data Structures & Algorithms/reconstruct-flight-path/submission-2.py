class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj=defaultdict(list)
        tickets.sort()
        for src,dest in tickets:
            adj[src].append(dest)

        res=collections.deque()
        def dfs(src):
            while adj[src]:
                curr=adj[src].pop(0)
                dfs(curr)
            res.appendleft(src)
        dfs("JFK")
        return list(res)