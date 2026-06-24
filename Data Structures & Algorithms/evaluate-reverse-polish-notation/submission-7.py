class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk=[]
        for i in tokens:
            operators={'-','+','/','*'}
            if i not in operators:
                stk.append(int(i))
            elif i=='+':
                stk.append(int(stk.pop())+int(stk.pop()))
            elif i=='-':
                a=int(stk.pop())
                b=int(stk.pop())
                stk.append(b-a)
            elif i=='/':
                a=int(stk.pop())
                b=int(stk.pop())
                stk.append(int(b/a))
            elif i=='*':
                stk.append(int(stk.pop())*int(stk.pop()))
        return stk[-1]