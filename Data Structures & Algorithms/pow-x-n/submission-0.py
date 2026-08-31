class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,power):
            if x==0:return 0
            if power==0: return 1
            
            res=helper(x,power//2)
            res=res*res

            return res*x if power%2 else res
        res=helper(x,abs(n))
        return res if n>=0 else 1/res