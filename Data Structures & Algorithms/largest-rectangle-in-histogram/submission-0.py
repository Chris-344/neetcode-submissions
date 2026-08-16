class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk=[]
        res=0

        for i in range(len(heights)):
            curr=i
            while stk and heights[i]<stk[-1][1]:
                idx,val=stk.pop()
                res=max(res,val*(i-idx))            
                curr=idx
            
            stk.append((curr,heights[i]))

        while stk:
            idx,val=stk.pop()
            res=max(res,val*(len(heights)-idx))

        return res