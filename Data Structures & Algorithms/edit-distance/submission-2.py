class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp={}
        def dfs(a:str,b:str):
            if (a,b) in dp:
                return dp[(a,b)]
            if a==b:
                dp[(a,b)]=0
                dp[(b,a)]=0
            elif a in b:
                dp[(a,b)]=len(b)-len(a)
                dp[(b,a)]=len(b)-len(a)
            elif b in a:
                dp[(a,b)]=len(a)-len(b)
                dp[(b,a)]=len(a)-len(b)
            elif a[0]==b[0]:
                dp[(a,b)]=dfs(a[1:],b[1:])
            elif a[0]!=b[0]:
                dp[(a,b)] = 1 + min(dfs(a[1:],b),dfs(a,b[1:]),dfs(a[1:],b[1:]))
            return dp[(a,b)]
        return dfs(word1,word2)