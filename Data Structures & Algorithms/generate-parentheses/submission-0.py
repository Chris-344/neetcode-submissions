class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stk=[]
        res=[]

        def dfs(openN,closeN):
            if openN==closeN==n:
                res.append("".join(stk))
                return
            if openN < n:
                stk.append("(")
                dfs(openN+1,closeN)
                stk.pop()
            if closeN<openN:
                stk.append(")")
                dfs(openN,closeN+1)
                stk.pop()
        dfs(0,0)
        return res