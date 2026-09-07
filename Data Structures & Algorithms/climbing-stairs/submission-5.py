class Solution:
    def climbStairs(self, n: int) -> int:
        s1=1
        s2=2
        for _ in range(1,n):
            temp=s2
            s2=s1+s2
            s1=temp

        return s1