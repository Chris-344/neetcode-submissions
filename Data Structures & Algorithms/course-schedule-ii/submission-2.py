class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj={i:[] for i in range(numCourses)}
        
        for crs,pre in prerequisites:
            adj[crs].append(pre)
        
        res=[]
        cur,completed=set(),set()

        def dfs(crs):
            if crs in cur:
                return False
            if crs in completed:
                return True
            cur.add(crs) 
            for i in adj[crs]:
                if dfs(i)==False:
                    return False
            cur.remove(crs)
            res.append(crs)
            completed.add(crs)

        for i in range(numCourses):
            if dfs(i)==False:
                return []
        return res

        