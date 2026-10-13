class Solution:
    def longestPalindrome(self, s: str) -> str:

        maxLen=0
        self.res=""
        for i in range(len(s)):
            l=r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 >=maxLen:
                    self.res=s[l:r+1]
                maxLen=max(r-l+1,maxLen)
                l-=1
                r+=1
        
        for i in range(len(s)):
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 >=maxLen:
                    self.res=s[l:r+1]
                maxLen=max(r-l+1,maxLen)
                l-=1
                r+=1
        
        return self.res