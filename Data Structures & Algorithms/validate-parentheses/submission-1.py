class Solution:
    def isOpen(self,c:str)->bool:
        return c=="[" or c=="(" or c=="{"
    def isMatch(self,a,b):
        obj= {')':'(','}':'{',']':'['}

        return obj[a]==b

    def isValid(self, s: str) -> bool:
        stk=[]

        for i in s:
            if self.isOpen(i):
                stk.append(i)
            else:
                if len(stk)!=0 and self.isMatch(i,stk[-1]):
                    stk.pop()
                else:
                    return False

        if len(stk)==0:
            return True
        return False