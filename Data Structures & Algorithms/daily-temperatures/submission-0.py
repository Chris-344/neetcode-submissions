class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk=[]
        res=[0]*len(temperatures)
        for i,j in enumerate(temperatures):
            if not stk:
                stk.append(i)
                continue
            elif temperatures[stk[-1]] > j:
                stk.append(i)
                continue
            while stk and temperatures[stk[-1]] < j:
                res[stk[-1]]=i-stk[-1]
                stk.pop()
                
            stk.append(i)
            
        return res

#3,2,5,3


#2,1,0,0