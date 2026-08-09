class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        myMap={}
        l,r=0,0
        res=0
        maxV=0

        while r<len(s):
            myMap[s[r]]=1 + myMap.get(s[r],0)
            maxV=max(myMap.values())            
            while (r-l+1) - maxV > k and l<r:
                myMap[s[l]]=myMap[s[l]] - 1
                maxV=max(myMap.values())
                l+=1
            res=max(res,r-l+1)
            
            
            r+=1
        return res