class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]

        for ch in s:
            if ch in "{([":
                stk.append(ch)
            elif not stk or (ch ==")" and stk[-1]!="(" or
                ch =="}" and stk[-1]!="{" or
                ch =="]" and stk[-1]!="[" ):
                return False
            else:
                stk.pop()
        return not stk