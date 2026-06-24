class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while (l<r):
            while (l<r and not self.isAlNum(s[l])):
                l+=1
            while (r>l and not self.isAlNum(s[r])):
                r-=1
            if s[r].lower()!=s[l].lower():
                return False
            r-=1
            l+=1
        return True


    def isAlNum(self,x):
        return (ord("A") <= ord(x) <=ord("Z") or 
        ord("a") <= ord(x) <=ord("z") or 
        ord("0") <= ord(x) <=ord("9"))
        