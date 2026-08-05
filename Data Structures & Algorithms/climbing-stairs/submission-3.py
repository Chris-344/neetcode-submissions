class Solution:
    def climbStairs(self, n: int) -> int:
        step1,step2=1,2
        if n<=2:
            return n
        for i in range(2,n):
            temp=step1
            step1=step2
            step2=temp+step2

        return step2