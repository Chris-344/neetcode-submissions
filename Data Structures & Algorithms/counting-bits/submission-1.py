class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[0]*(n+1)
        for i in range(1,n+1):
            if (i & (i-1))==0:
                res[i]=1
            elif i%2==0:
                res[i]=res[i//2]
            else:
                res[i]=res[i-1]+1
        return res

#0,1,1,2,1,2,2,3,1,2,2,3,3,2,2
#1,2,2,3,2,3,
#11=8+2+1