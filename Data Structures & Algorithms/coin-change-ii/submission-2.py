class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0]*(amount+1)
        dp[-1]=1
        for n in range(len(coins)-1,-1,-1):
            newDp=[0]*(amount+1)
            newDp[-1]=1
            for i in range(len(newDp)-2,-1,-1):
                if i+coins[n]<len(newDp):
                    newDp[i]=dp[i]+newDp[i+coins[n]]
                else:
                    newDp[i]=dp[i]
            dp=newDp
        return dp[0]