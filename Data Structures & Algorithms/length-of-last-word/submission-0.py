class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res=0
        s=s.strip()

        for i in range(len(s)-1,-1,-1):
        
            if s[i]==" ":
                break
            res+=1
        return res
            