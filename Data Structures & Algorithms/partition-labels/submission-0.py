class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex={}
        for i,ch in enumerate(s):
            lastIndex[ch]=i
        res=[]
        size,end=0,0

        for i,c in enumerate(s):
            size+=1

            end=max(lastIndex[c],end)            
            if i==end:
                res.append(size)
                size=0
        return res