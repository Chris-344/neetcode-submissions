class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N=len(edges)
        par=[i for i in range(N + 1)]
        rank=[1] * (N + 1)

        def find(n):
            if n!=par[n]:
                par[n]=find(par[n])
            return par[n]
        
        def union(n1,n2):
            v1,v2=find(n1),find(n2)

            if v1==v2:
                return False
            
            if rank[v1]>rank[v2]:
                par[v2]=v1
                rank[v1]+=rank[v2]
            else:
                par[v1]=v2
                rank[v2]+=rank[v1]

            return True


        for i,j in edges:
            if not union(i,j):
                return [i,j]