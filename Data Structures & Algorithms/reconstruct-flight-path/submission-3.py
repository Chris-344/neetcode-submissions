class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj=defaultdict(list)
        tickets.sort(reverse=True)
        for src,dest in tickets:
            adj[src].append(dest)

        res=collections.deque()
        def dfs(src):
            while adj[src]:
                curr=adj[src].pop()
                dfs(curr)
            res.appendleft(src)
        dfs("JFK")
        return list(res)